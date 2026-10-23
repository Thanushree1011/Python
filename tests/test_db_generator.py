
import unittest
from unittest.mock import MagicMock, patch

from db_generator import fetch_employees


class TestDatabaseGenerator(unittest.TestCase):

    @patch("db_generator.mysql.connector.connect")
    def test_fetches_employees(self, mock_connect):
        connection = MagicMock()
        cursor = MagicMock()

        mock_connect.return_value = connection
        connection.cursor.return_value = cursor

        cursor.fetchmany.side_effect = [
            [(1, "Amy", "Lee"), (2, "Ben", "Roy")],
            [(3, "Sam", "Das")],
            [],
        ]

        config = {
            "database": {
                "host": "localhost",
                "user": "root",
                "password": "test",
                "database": "employees",
            }
        }

        result = list(fetch_employees(batch_size=2))
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], (1, "Amy", "Lee"))
        self.assertEqual(result[2], (3, "Sam", "Das"))

        cursor.close.assert_called_once()
        connection.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
