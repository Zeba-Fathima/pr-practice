from utils import validate_amount

LARGE_REFUND_THRESHOLD = 1000


def process_refund(amount, user_id):
    valid = validate_amount(amount)
    return {"user": user_id, "refund": valid, "status": "refunded"}


def process_large_refund(amount, user_id):
    valid = validate_amount(amount)
    if valid < LARGE_REFUND_THRESHOLD:
        raise ValueError(f"Amount {valid} is below the large-refund threshold")
    return {
        "user": user_id,
        "refund": valid,
        "status": "refunded",
        "requires_approval": True,
    }

