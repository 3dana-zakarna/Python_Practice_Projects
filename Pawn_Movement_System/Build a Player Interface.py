
import random
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)

        x = self.position[0] + move[0]
        y = self.position[1] + move[1]

        self.position = (x, y)
        self.path.append(self.position)

        return self.position

    @abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
            (0, 1),   # Up
            (0, -1),  # Down
            (-1, 0),  # Left
            (1, 0)    # Right
        ]

    def level_up(self):
        self.moves.extend([
            (-1, 1),   # Up-left
            (1, 1),    # Up-right
            (-1, -1),  # Down-left
            (1, -1)    # Down-right
        ])


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1: INITIALIZATION ==========")
    pawn = Pawn()

    assert pawn.moves == [
        (0, 1), (0, -1), (-1, 0), (1, 0)
    ]
    assert pawn.position == (0, 0)
    assert pawn.path == [(0, 0)]

    print("Initialization test passed!")

    print("\n========== TEST 2: MAKE MOVE ==========")
    new_position = pawn.make_move()

    assert new_position == pawn.position
    assert len(pawn.path) == 2
    assert pawn.path[-1] == pawn.position

    print("New position:", new_position)
    print("Path:", pawn.path)
    print("Make move test passed!")

    print("\n========== TEST 3: LEVEL UP ==========")
    original_moves = len(pawn.moves)
    pawn.level_up()

    assert len(pawn.moves) == original_moves + 4
    assert (-1, 1) in pawn.moves
    assert (1, 1) in pawn.moves
    assert (-1, -1) in pawn.moves
    assert (1, -1) in pawn.moves

    print("Available moves after level up:", pawn.moves)
    print("Level up test passed!")

    print("\n========== TEST 4: MULTIPLE MOVES ==========")
    for _ in range(5):
        pawn.make_move()

    assert len(pawn.path) == 7

    print("Final position:", pawn.position)
    print("Complete path:", pawn.path)
    print("Multiple moves test passed!")

    print("\n========== TEST 5: ABSTRACT CLASS ==========")
    try:
        Player()
        assert False, "Player should be abstract"
    except TypeError:
        print("Player is correctly defined as an abstract class.")

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()
