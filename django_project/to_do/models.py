from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    
    def __str__(self):
        return self.task_text
    