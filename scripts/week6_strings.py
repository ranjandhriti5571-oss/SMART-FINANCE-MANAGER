def format_transaction(t):
    return f"ID:{t['id']} {t['type']} {t['amount']} ({t['category']})"
