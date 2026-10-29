# Discount Strategy Engine

## Description
A Python-based discount calculation system that applies different discount strategies to products and determines the best available price for a customer based on applicable discounts and membership tier.

The project uses object-oriented programming and the Strategy Design Pattern to implement flexible and reusable discount rules.

## Features
- **Product Management:** Represent products with names and prices.
- **Percentage Discounts:** Calculate discounts based on a percentage of the original price.
- **Fixed-Amount Discounts:** Reduce product prices by a specified amount when eligible.
- **Premium Membership Discounts:** Apply special pricing for premium users.
- **Discount Eligibility:** Check whether each discount strategy can be applied.
- **Best Price Calculation:** Compare applicable discounted prices with the original price and return the lowest option.
- **Automated Testing:** Verify product behavior, discount calculations, eligibility rules, and the discount engine.

## Concepts Used
- Python Object-Oriented Programming (OOP)
- Classes and Objects
- Abstract Base Classes (ABC)
- Inheritance and Method Overriding
- Abstract Methods
- Strategy Design Pattern
- Type Hints
- List Comprehensions
- Conditional Statements
- Unit Testing with Assertions

## How It Works
1. A product is created with a name and price.
2. Different discount strategies define their own eligibility rules and price calculations.
3. The discount engine evaluates the available strategies for the customer.
4. The engine compares the eligible discounted prices with the original price.
5. The lowest available price is returned.

## Example

```python
product = Product("Wireless Mouse", 50.0)

strategies = [
    PercentageDiscount(10),
    FixedAmountDiscount(5),
    PremiumUserDiscount()
]

engine = DiscountEngine(strategies)

best_price = engine.calculate_best_price(product, "Premium")
print(f"Best price: ${best_price:.2f}")
```

Output:

```text
Best price: $40.00
```

## How to Run
1. Install Python 3.9 or later.
2. Save the program in a Python file.
3. Run the file from your terminal:

   ```bash
   python discount_engine.py
   ```

The program executes the included test cases and displays the results.

## Purpose
This project demonstrates how the Strategy Design Pattern and object-oriented programming can be used to build a flexible discount system that supports multiple pricing rules and customer membership tiers.

**Language:** Python 3
