from scripts.week1_basics import welcome
from scripts.week2_io import get_transaction
from scripts.week3_conditions import validate
from scripts.week4_loops import display
from scripts.week5_functions import generate_id
from scripts.week7_data_structures import create_transaction
from scripts.week8_advanced_ds import calculate_balance
from scripts.week10_files import load, save
from scripts.week11_exceptions import safe_input
from scripts.week12_analytics import report

def main():
    welcome()
    data = load()

    while True:
        print("\n1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Balance")
        print("4. Report")
        print("5. Exit")

        choice = safe_input()

        if choice == 1:
            t_type, amount, category = get_transaction()
            if validate(t_type, amount):
                tid = generate_id(data)
                t = create_transaction(tid, t_type, amount, category)
                data.append(t)
                save(data)

        elif choice == 2:
            display(data)

        elif choice == 3:
            print("Balance:", calculate_balance(data))

        elif choice == 4:
            report(data)

        elif choice == 5:
            break

if __name__ == "__main__":
    main()
