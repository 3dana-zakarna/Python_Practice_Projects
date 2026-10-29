
import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"

        return picture

    def get_amount_inside(self, shape):
        return (
            (self.width // shape.width)
            * (self.height // shape.height)
        )

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== RECTANGLE TESTS ==========")

    rect = Rectangle(10, 5)

    assert rect.get_area() == 50
    assert rect.get_perimeter() == 30
    assert rect.get_diagonal() == math.sqrt(125)
    assert str(rect) == "Rectangle(width=10, height=5)"

    rect.set_height(3)
    assert rect.get_perimeter() == 26
    assert str(rect) == "Rectangle(width=10, height=3)"

    print(rect)
    print(rect.get_picture())

    print("Rectangle tests passed!")

    print("\n========== SQUARE TESTS ==========")

    sq = Square(9)

    assert sq.get_area() == 81
    assert str(sq) == "Square(side=9)"

    sq.set_side(4)
    assert sq.get_area() == 16
    assert sq.get_diagonal() == math.sqrt(32)
    assert str(sq) == "Square(side=4)"

    sq.set_width(5)
    assert sq.width == 5 and sq.height == 5

    sq.set_height(3)
    assert sq.width == 3 and sq.height == 3

    print(sq)
    print(sq.get_picture())

    print("Square tests passed!")

    print("\n========== AMOUNT INSIDE TESTS ==========")

    rect = Rectangle(15, 10)
    assert rect.get_amount_inside(Square(5)) == 6

    rect = Rectangle(4, 8)
    assert rect.get_amount_inside(Rectangle(3, 6)) == 1

    rect = Rectangle(2, 3)
    assert rect.get_amount_inside(Rectangle(3, 6)) == 0

    print("Amount inside tests passed!")

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()
