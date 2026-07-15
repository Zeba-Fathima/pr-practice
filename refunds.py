from utils import validate_amount

def process_refund(amount, user_id):
    valid = validate_amount(amount)
    return {"user": user_id, "refund": valid, "status": "refunded"}