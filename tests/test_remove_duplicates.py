import unittest

from remove_duplicates import remove_duplicates


class TestRemoveDuplicates(unittest.TestCase):

    def test_removes_duplicates(self):
        self.assertEqual(
            remove_duplicates([1, 2, 1, 3, 2]),
            [1, 2, 3],
        )

    def test_preserves_order(self):
        self.assertEqual(
            remove_duplicates(["b", "a", "b", "c"]),
            ["b", "a", "c"],
        )

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()