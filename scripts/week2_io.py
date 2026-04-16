def get_transaction():
    t_type = input('Type (income/expense): ')
    amount = float(input('Amount: '))
    category = input('Category: ')
    return t_type, amount, category
