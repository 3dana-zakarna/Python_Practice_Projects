# Budget App & Spending Chart

## Description
A Python budget management application that allows users to manage expenses across different spending categories. It supports deposits, withdrawals, fund transfers between categories, balance tracking, and generating a visual chart showing the percentage of total spending for each category.

## Features
- **Create Budget Categories:** Organize transactions into categories such as Food, Clothing, and Entertainment.
- **Deposit Funds:** Add money to a category's budget.
- **Withdraw Funds:** Record expenses while checking available funds.
- **Transfer Money:** Move money between categories and track both sides of the transaction.
- **Check Balances:** Calculate the current balance of each category.
- **Transaction Ledger:** Store transaction amounts and descriptions.
- **Spending Visualization:** Generate a vertical bar chart showing each category's percentage of total spending.
- **Automated Testing:** Run test cases to verify deposits, withdrawals, transfers, balance calculations, and chart generation.

## Concepts Used
- Python Object-Oriented Programming (OOP)
- Classes and Objects
- Lists and Dictionaries
- Methods and Functions
- Loops and Conditional Statements
- String Formatting and Alignment
- Data Processing and Calculations
- Assertions and Unit Testing

## How to Run
1. Make sure Python 3 is installed.
2. Save the program as a `.py` file.
3. Run the following command in your terminal:

   ```bash
   python budget_app.py
   ```

The program runs the included test cases and displays their results, along with a sample spending chart.

## Example Usage

```python
food = Category("Food")
food.deposit(1000, "Initial deposit")
food.withdraw(150, "Groceries")

clothing = Category("Clothing")
food.transfer(100, clothing)

print(food)
print(clothing)

print(create_spend_chart([food, clothing]))
```

## Purpose
This project demonstrates how Python classes can be used to manage financial transactions, organize budget data, validate available funds, and visualize spending distributions.

**Language:** Python 3
