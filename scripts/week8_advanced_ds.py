def calculate_balance(data):
    balance = 0
    for t in data:
        if t['type']=='income': balance += t['amount']
        else: balance -= t['amount']
    return balance
