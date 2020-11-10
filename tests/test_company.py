import unittest
from models.company import Company

class TestCompany(unittest.TestCase):
    def setUp(self):
        self.company = Company("Trumps Business", 1)
        self.company1 = Company("Trumps Business")

    def test_company_has_name(self):
        self.assertEqual("Trumps Business", self.company.name)

    def test_company_has_id(self):
        self.assertEqual(1, self.company.id)

    def test_company_default_id(self):
        self.assertEqual(None, self.company1.id)
