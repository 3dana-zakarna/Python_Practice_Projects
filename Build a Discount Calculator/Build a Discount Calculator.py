
from abc import ABC, abstractmethod


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'


class DiscountStrategy(ABC):
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: int) -> None:
        self.percent = percent

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return self.percent <= 70

    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return product.price * 0.9 > self.amount

    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount


class PremiumUserDiscount(DiscountStrategy):
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return user_tier.lower() == 'premium'

    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8


class DiscountEngine:
    def __init__(self, strategies: list[DiscountStrategy]) -> None:
        self.strategies = strategies

    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        prices = [product.price]

        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)

        return min(prices)


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1: PRODUCT ==========")
    product = Product("Wireless Mouse", 50.0)

    assert product.name == "Wireless Mouse"
    assert product.price == 50.0
    assert str(product) == "Wireless Mouse - $50.0"

    print(product)
    print("Product test passed!\n")

    print("========== TEST 2: PERCENTAGE DISCOUNT ==========")
    percentage = PercentageDiscount(10)

    assert percentage.is_applicable(product, "Regular") is True
    assert percentage.apply_discount(product) == 45.0

    print("Price after 10% discount:", percentage.apply_discount(product))
    print("Percentage discount test passed!\n")

    print("========== TEST 3: PERCENTAGE DISCOUNT LIMIT ==========")
    percentage_70 = PercentageDiscount(70)
    percentage_80 = PercentageDiscount(80)

    assert percentage_70.is_applicable(product, "Regular") is True
    assert percentage_80.is_applicable(product, "Regular") is False

    print("Percentage limit test passed!\n")

    print("========== TEST 4: FIXED AMOUNT DISCOUNT ==========")
    fixed = FixedAmountDiscount(5)

    assert fixed.is_applicable(product, "Regular") is True
    assert fixed.apply_discount(product) == 45.0

    print("Price after $5 discount:", fixed.apply_discount(product))
    print("Fixed amount discount test passed!\n")

    print("========== TEST 5: FIXED DISCOUNT NOT APPLICABLE ==========")
    large_fixed = FixedAmountDiscount(50)

    assert large_fixed.is_applicable(product, "Regular") is False

    print("Fixed discount eligibility test passed!\n")

    print("========== TEST 6: PREMIUM USER DISCOUNT ==========")
    premium = PremiumUserDiscount()

    assert premium.is_applicable(product, "Premium") is True
    assert premium.is_applicable(product, "premium") is True
    assert premium.is_applicable(product, "Regular") is False
    assert premium.apply_discount(product) == 40.0

    print("Price after premium discount:", premium.apply_discount(product))
    print("Premium discount test passed!\n")

    print("========== TEST 7: DISCOUNT ENGINE ==========")
    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount()
    ]

    engine = DiscountEngine(strategies)
    best_price = engine.calculate_best_price(product, "Premium")

    assert best_price == 40.0

    print(f"Original price: ${product.price:.2f}")
    print(f"Best price: ${best_price:.2f}")
    print("Discount engine test passed!\n")

    print("========== TEST 8: REGULAR USER ==========")
    regular_price = engine.calculate_best_price(product, "Regular")

    assert regular_price == 45.0

    print(f"Regular user best price: ${regular_price:.2f}")
    print("Regular user test passed!\n")

    print("========== TEST 9: NO DISCOUNTS ==========")
    no_discount_engine = DiscountEngine([])
    unchanged_price = no_discount_engine.calculate_best_price(
        product, "Regular"
    )

    assert unchanged_price == 50.0

    print(f"Price without discounts: ${unchanged_price:.2f}")
    print("No discounts test passed!\n")

    print("========== ALL TESTS PASSED! ==========")


if __name__ == '__main__':
    run_tests()
   