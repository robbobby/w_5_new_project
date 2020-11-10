import unittest
from models.project import Project

class TestProject(unittest.TestCase):
    def setUp(self):
        self.project = Project("First Project")
        self.project1 = Project("Second Project", 1)

    def test_project_has_name(self):
        self.assertEqual("First Project", self.project.name)

    def test_project_has_default_id(self):
        self.assertEqual(None, self.project.id)

    def test_project_changed_id(self):
        self.assertEqual(1, self.project1.id)