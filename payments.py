from utils import validate_amount

def process_payment(amount, user_id):
    valid = validate_amount(amount)
    return {"user": user_id, "amount": valid, "status": "ok"}