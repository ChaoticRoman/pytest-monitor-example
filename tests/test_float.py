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


if __name__ == '__main__':
    unittest.main()
