from dataclasses import dataclass
from decimal import Decimal


@dataclass
class QuoteLine:
    """One line on a Meridian quote.

    unit_price is a Decimal, not a float — quote totals are money, and money
    in a float is a defect waiting for quarter-end (see w0m3).
    """

    sku: str
    qty: int
    unit_price: Decimal
