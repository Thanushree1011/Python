import unittest

from squares import generate_squares


class TestSquares(unittest.TestCase):

    def test_squares_count(self):
        self.assertEqual(len(generate_squares()), 20)

    def test_first_and_last_squares(self):
        squares = generate_squares()
        self.assertEqual(squares[0], 1)
        self.assertEqual(squares[-1], 400)

    def test_all_squares(self):
        self.assertEqual(
            generate_squares(),
            [number ** 2 for number in range(1, 21)],
        )


if __name__ == "__main__":
    unittest.main()