import stripe

stripe.api_key = "~[STRIPE_SECRET_KEY_0]~"

def charge(amount: int, source: str, description: str):
    return stripe.Charge.create(
        amount=amount,
        currency="usd",
        source=source,
        description=description,
    )
