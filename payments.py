from utils import validate_amount


def process_payment(amount, user_id):
    valid = validate_amount(amount)
    return {"user": user_id, "amount": valid, "status": "ok"}


def process_batch(payments):
    results = []
    for p in payments:
        try:
            results.append(process_payment(p["amount"], p["user_id"]))
        except ValueError as exc:
            results.append({
                "user": p["user_id"],
                "amount": p["amount"],
                "status": "rejected",
                "error": str(exc),
            })
    return results


def get_user_balance(user_id):
    return 100
