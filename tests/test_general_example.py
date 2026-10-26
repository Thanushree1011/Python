
from unittest.mock import patch

from src.general_example import GeneralExample


def test_flatten_dictionary():
    content = {
        'key1': [3, 2, 1],
        'key2': [42, 55, 10],
        'key3': [0, 22],
    }

    expected = [0, 1, 2, 3, 10, 22, 42, 55]
    actual = GeneralExample.flatten_dictionary(content)

    assert actual == expected


def test_fetch_emp_details():
    employee = GeneralExample()
    mock_record = ['emp001', 'Sam', '100000']

    with patch.object(
        employee,
        'load_employee_rec_from_database',
        return_value=mock_record,
    ) as mock_database:
        actual = employee.fetch_emp_details()

    assert actual == {
        'empId': 'emp001',
        'empName': 'Sam',
        'empSalary': '100000',
    }
    mock_database.assert_called_once_with()
