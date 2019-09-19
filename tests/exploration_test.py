import unittest
import segement
# sut = __import__("__init__.py")


def summe(arg):
    total = 0
    for val in arg:
        total += val
    return total


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = summe(data)
        self.assertEqual(result, 6)

    def test_segement(self):
        time = segement.DESCRIPTION.get("time").get("top")
        self.assertEqual(time, "")


if __name__ == '__main__':
    unittest.main()
