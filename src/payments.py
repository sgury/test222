import os
import uuid
from typing import Optional

import stripe

MIN_AMOUNT_CENTS = 50  # Stripe minimum for USD


def _api_key() -> str:
    key = os.environ.get("STRIPE_SECRET_KEY")
    if not key:
        raise RuntimeError("STRIPE_SECRET_KEY environment variable is not set")
    return key


def charge(
    amount: int,
    source: str,
    description: str,
    currency: str = "usd",
    idempotency_key: Optional[str] = None,
):
    """Create a charge. `amount` is in the smallest currency unit (cents).

    Pass a stable `idempotency_key` per order so network retries never double-charge.
    """
    if isinstance(amount, bool) or not isinstance(amount, int):
        raise TypeError("amount must be an integer number of cents")
    if amount < MIN_AMOUNT_CENTS:
        raise ValueError(f"amount must be at least {MIN_AMOUNT_CENTS} cents")
    if not source:
        raise ValueError("source is required")

    return stripe.Charge.create(
        api_key=_api_key(),
        amount=amount,
        currency=currency,
        source=source,
        description=description,
        idempotency_key=idempotency_key or str(uuid.uuid4()),
    )
