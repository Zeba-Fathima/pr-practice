from utils import validate_amount

def process_refund(amount, user_id):
    valid = validate_amount(amount)
    return {"user": user_id, "refund": valid, "status": "refunded"}
 
def format_refund_date(d):
    return d.strftime("%d-%m-%Y")

def process_large_refund(amount, user_id):
    return {"user": user_id, "refund": amount, "status": "refunded"}