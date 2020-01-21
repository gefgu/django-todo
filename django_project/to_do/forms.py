from django import forms
from .models import Task

class TaskForm(forms.ModleForm):
    class Meta:
        model = Task
        fields = []

