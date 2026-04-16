def report(data):
    income = sum(t['amount'] for t in data if t['type']=='income')
    expense = sum(t['amount'] for t in data if t['type']=='expense')
    print('Total Income:', income)
    print('Total Expense:', expense)
