import unittest
from models.task import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task = Task("Coffee morning", "The whole team needs Coffee")
        self.task1 = Task("Coffee morning", "The whole team needs Coffee", 1, 100, True)

    def test_task_has_name(self):
        self.assertEqual("Coffee morning", self.task.name)

    def test_task_has_description(self):
        self.assertEqual("The whole team needs Coffee", self.task.description)

    def test_task_has_default_id(self):
        self.assertEqual(None, self.task.id)

    def test_task_changed_id(self):
        self.assertEqual(1, self.task1.id)

    def test_task_has_default_completed_amount(self):
        self.assertEqual(0, self.task.completed)

    def test_task_changed_init_completed_amount(self):
        self.assertEqual(100, self.task1.completed_amount)

    def test_task_default_completed(self):
        self.assertEqual(False, self.task.completed)

    def test_task_change_init_completed(self):
        self.assertEqual(True, self.task1.completed)