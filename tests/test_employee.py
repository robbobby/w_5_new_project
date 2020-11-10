import unittest
from models.employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Bob")
        self.employee1 = Employee("Barb", 1)

    def test_project_has_name(self):
        self.assertEqual("Bob", self.employee.name)

    def test_project_has_default_id(self):
        self.assertEqual(None, self.employee.id)

    def test_project_changed_id(self):
        self.assertEqual(1, self.employee1.id)