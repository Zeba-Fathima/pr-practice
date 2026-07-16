from utils import validate_amount


def process_payouts(payouts):
    """Pay out a batch of amounts and return the total."""
    total = 0
    for p in payouts:
        total += validate_amount(p["amount"])
    return total
