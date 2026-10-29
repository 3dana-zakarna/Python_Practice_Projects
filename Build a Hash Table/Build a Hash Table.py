
class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(char) for char in string)

    def add(self, key, value):
        hash_value = self.hash(key)

        if hash_value not in self.collection:
            self.collection[hash_value] = {}

        self.collection[hash_value][key] = value

    def remove(self, key):
        hash_value = self.hash(key)

        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]

    def lookup(self, key):
        hash_value = self.hash(key)

        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                return self.collection[hash_value][key]

        return None


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1: INITIALIZATION ==========")
    ht = HashTable()
    assert ht.collection == {}
    print("Initialization test passed!")

    print("\n========== TEST 2: HASH FUNCTION ==========")
    assert ht.hash("A") == 65
    assert ht.hash("abc") == 294
    assert ht.hash("") == 0
    print("Hash function test passed!")

    print("\n========== TEST 3: ADD AND LOOKUP ==========")
    ht.add("name", "Dana")
    ht.add("age", 20)

    assert ht.lookup("name") == "Dana"
    assert ht.lookup("age") == 20
    print("Add and lookup tests passed!")

    print("\n========== TEST 4: LOOKUP MISSING KEY ==========")
    assert ht.lookup("missing") is None
    print("Missing key test passed!")

    print("\n========== TEST 5: UPDATE EXISTING KEY ==========")
    ht.add("name", "Sajad")
    assert ht.lookup("name") == "Sajad"
    print("Update test passed!")

    print("\n========== TEST 6: REMOVE KEY ==========")
    ht.remove("age")
    assert ht.lookup("age") is None
    assert ht.lookup("name") == "Sajad"
    print("Remove test passed!")

    print("\n========== TEST 7: REMOVE MISSING KEY ==========")
    ht.remove("missing")
    assert ht.lookup("name") == "Sajad"
    print("Remove missing key test passed!")

    print("\n========== TEST 8: HASH COLLISIONS ==========")
    # "ab" and "ba" have the same hash value.
    ht.add("ab", 100)
    ht.add("ba", 200)

    assert ht.hash("ab") == ht.hash("ba")
    assert ht.lookup("ab") == 100
    assert ht.lookup("ba") == 200

    ht.remove("ab")
    assert ht.lookup("ab") is None
    assert ht.lookup("ba") == 200
    print("Collision tests passed!")

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()
