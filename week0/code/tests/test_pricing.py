from decimal import Decimal

from quoting.models import QuoteLine
from quoting.pricing import quote_total, round_currency


def test_quote_total_under_threshold_has_no_discount():
    line = QuoteLine(sku="MRD-1001", qty=50, unit_price=Decimal("10.00"))
    assert quote_total([line]) == Decimal("500.00")


def test_volume_discount_applies_at_100_units():
    """Meridian's policy (section 4.2) applies the discount at 100 units or
    more — 'or more' means the boundary itself qualifies."""
    line = QuoteLine(sku="MRD-44821-B", qty=100, unit_price=Decimal("45.00"))
    assert quote_total([line]) == Decimal("4275.00")


def test_volume_discount_applies_above_threshold_too():
    line = QuoteLine(sku="MRD-44821-B", qty=150, unit_price=Decimal("45.00"))
    assert quote_total([line]) == Decimal("6412.50")


def test_round_currency_rounds_half_up_on_penny_boundary():
    """Meridian's finance team requires round-half-up, not whatever the
    platform's float rounding happens to do at a given boundary."""
    assert round_currency(Decimal("1000.045")) == Decimal("1000.05")
