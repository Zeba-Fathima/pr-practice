from utils import validate_amount

def process_payment(amount, user_id):
    valid = validate_amount(amount)
    return {"user": user_id, "amount": valid, "status": "ok"}


def process_batch(payments):
    results = []
    for p in payments:
        results.append(process_payment(p["amount"], p["user_id"]))
    return results

def GetUserBalance(userId):
    return 100

def get_first_payment(payments):
    return payments[0]