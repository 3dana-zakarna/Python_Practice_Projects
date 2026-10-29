
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*")
        items = ""

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + "\n" + items + total


def create_spend_chart(categories):
    total_spent = 0
    spent = []

    # Calculate total spending for each category
    for category in categories:
        category_spent = 0

        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += abs(item["amount"])

        spent.append(category_spent)
        total_spent += category_spent

    # Calculate percentages rounded down to the nearest 10
    percentages = []

    for amount in spent:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentage = int(amount / total_spent * 100)
            percentage = percentage // 10 * 10
            percentages.append(percentage)

    # Chart title
    chart = "Percentage spent by category\n"

    # Vertical bar chart
    for percentage in range(100, -1, -10):
        chart += f"{percentage:>3}|"

        for value in percentages:
            if value >= percentage:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    max_name_length = max(
        len(category.name) for category in categories
    )

    for i in range(max_name_length):
        line = "     "

        for category in categories:
            if i < len(category.name):
                line += category.name[i] + "  "
            else:
                line += "   "

        chart += line + "\n"

    return chart.rstrip("\n")


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1: DEPOSIT ==========")
    food = Category("Food")
    food.deposit(100, "Initial deposit")

    assert food.get_balance() == 100
    print("Deposit test passed!")

    print("\n========== TEST 2: WITHDRAW ==========")
    result = food.withdraw(30, "Groceries")

    assert result is True
    assert food.get_balance() == 70
    print("Withdraw test passed!")

    print("\n========== TEST 3: INSUFFICIENT FUNDS ==========")
    result = food.withdraw(200, "Expensive purchase")

    assert result is False
    assert food.get_balance() == 70
    print("Insufficient funds test passed!")

    print("\n========== TEST 4: TRANSFER ==========")
    clothing = Category("Clothing")
    result = food.transfer(20, clothing)

    assert result is True
    assert food.get_balance() == 50
    assert clothing.get_balance() == 20
    print("Transfer test passed!")

    print("\n========== TEST 5: CHECK FUNDS ==========")
    assert food.check_funds(40) is True
    assert food.check_funds(100) is False
    print("Check funds test passed!")

    print("\n========== TEST 6: CATEGORY STRING ==========")
    assert "Total: 50.00" in str(food)
    print(food)
    print("String representation test passed!")

    print("\n========== TEST 7: SPENDING CHART ==========")
    food_chart = Category("Food")
    food_chart.deposit(1000, "Deposit")
    food_chart.withdraw(100, "Groceries")
    food_chart.withdraw(200, "Restaurant")

    entertainment = Category("Entertainment")
    entertainment.deposit(500, "Deposit")
    entertainment.withdraw(100, "Movies")

    clothing_chart = Category("Clothing")
    clothing_chart.deposit(300, "Deposit")
    clothing_chart.withdraw(100, "Shirts")

    categories = [food_chart, entertainment, clothing_chart]
    chart = create_spend_chart(categories)

    print(chart)

    assert "Percentage spent by category" in chart

    # Verify category letters, since names are printed vertically
    for category in categories:
        for letter in category.name:
            assert letter in chart

    print("\nSpending chart test passed!")
    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()

