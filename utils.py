def format_date(d):
    """Format a date as DD-MM-YYYY."""
    return d.strftime("%d-%m-%Y")


def validate_amount(amount):
    """Validate a payment amount. Raises ValueError if negative."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    return amount
