"""Basic example adpated from official documentation [1].

[1]: https://docs.python.org/3/library/unittest.html
"""
import unittest


class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up the class.")

    def setUp(self):
        print("Setting up the test.")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            float("")

    def test_invalid_string(self):
        with self.assertRaises(ValueError):
            float("xyz")

    def test_correct_string(self):
        result = float("0.5")
        self.assertEqual(result, 0.5)

    def test_allocate_1MB(self):
        megabyte_array()


    def test_allocate_100MB(self):
        megabyte_array(100)


def megabyte_array(megabytes=1):
    count = megabytes * (2**20 // 8)  # Python uses 8 byte integers
    return [0 for _ in range(count)]


tests = TestStringMethods()


def test_empty_string():
    tests.test_empty_string()


if __name__ == '__main__':
    unittest.main()
