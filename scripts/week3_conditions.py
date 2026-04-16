def validate(t_type, amount):
    if t_type in ['income','expense'] and amount > 0:
        return True
    print('Invalid transaction')
    return False
