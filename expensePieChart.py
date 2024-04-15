
# CS-175L-02
# Leslie Bustamante
# expensesPieChart

import matplotlib.pyplot as plt

def read_expenses(filename):
    expenses = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                category, amount_str = line.strip().split('\t')
                try:
                    amount = int(amount_str)
                    expenses[category] = amount
                except ValueError:
                    print(f"Value Error: Could not convert '{amount_str}' to integer for category '{category}'.")
    except IOError:
        print(f"IOError: Could not open the file '{filename}'.")

    return expenses

def plot_pie_chart(expenses):
    labels = expenses.keys()
    amounts = expenses.values()

    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=labels, startangle=140)
    plt.title('Monthly Expenses')
    plt.axis('equal')  
    plt.show()

def main():
    filename = 'expenses.txt'
    expenses = read_expenses(filename)
    plot_pie_chart(expenses)

if __name__ == "__main__":
    main()
