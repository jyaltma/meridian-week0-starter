"""Meridian quote pricing.

Policy (from Meridian's pricing team, 2026 revision, section 4.2):
  - Quotes totalling 100 units or more across all lines receive a 5% volume
    discount on the subtotal.
  - All monetary totals round to the nearest cent, half up (never banker's
    rounding), because that is what Meridian's finance team's reconciliation
    tooling expects.
"""

from decimal import ROUND_HALF_UP, Decimal

from quoting.models import QuoteLine

VOLUME_DISCOUNT_THRESHOLD = 100
VOLUME_DISCOUNT_RATE = Decimal("0.05")


def total_units(lines: list[QuoteLine]) -> int:
    """Total quantity across every line on the quote."""
    return sum(line.qty for line in lines)


def apply_volume_discount(subtotal: Decimal, total_qty: int) -> Decimal:
    """Apply Meridian's volume discount to a subtotal, if the quote qualifies."""
    if total_qty >= VOLUME_DISCOUNT_THRESHOLD:
        return subtotal * (Decimal("1") - VOLUME_DISCOUNT_RATE)
    return subtotal


def round_currency(amount: Decimal) -> Decimal:
    """Round a monetary amount to the nearest cent."""
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def quote_total(lines: list[QuoteLine]) -> Decimal:
    """Total for a quote. Pure: does not modify lines."""
    subtotal = sum((line.unit_price * line.qty for line in lines), Decimal("0"))
    discounted = apply_volume_discount(subtotal, total_units(lines))
    return round_currency(discounted)
