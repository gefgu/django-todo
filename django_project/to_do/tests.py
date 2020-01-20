from django.test import TestCase

from .models import Task
from django.utils import timezone

# Create your tests here.
class ToDoModelTests(TestCase):
    def test_text_field(self):
        text_field = "Task #1"
        task = Task(task_text=text_field)
        self.assertEqual(task.task_text, text_field)
        
    def test_date_field(self):
        date = timezone.now()
        task = Task(task_text="#", pub_date=date)
        self.assertEqual(task.pub_date, date)
        