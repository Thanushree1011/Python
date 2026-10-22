from unittest import TestCase
import unittest
from person import Male,Female,Person

class TestPerson(TestCase):
    def test_male_get_gender(self):
        male = Male()
        self.assertEqual(male.get_gender(), "Male")

    def test_female_get_gender(self):
        female = Female()
        self.assertEqual(female.get_gender(), "Female")

    def test_person_is_abstract(self):
        with self.assertRaises(TypeError):
            Person()  # Should raise TypeError because Person is abstract

if __name__ == "__main__":
    unittest.main()