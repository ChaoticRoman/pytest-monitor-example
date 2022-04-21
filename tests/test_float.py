"""Basic example adpated from official documentation [1].

[1]: https://docs.python.org/3/library/unittest.html
"""
import unittest


class TestStringMethods(unittest.TestCase):

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            float("")

    def test_invalid_string(self):
        with self.assertRaises(ValueError):
            float("xyz")

    def test_correct_string(self):
        result = float("0.5")
        self.assertEqual(result, 0.5)


def test_empty_string():
    try:
        float("")
    except ValueError:
        pass
    else:
        raise AssertionError("Error: Should have raised ValueError.")


def megabyte_array(megabytes=1):
    count = megabytes * (2**20 // 8)  # Python uses 8 byte integers
    return [0 for _ in range(count)]


def test_allocate_1MB():
    megabyte_array()


def test_allocate_100MB():
    megabyte_array(100)


if __name__ == '__main__':
    unittest.main()
