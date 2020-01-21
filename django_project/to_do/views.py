from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    form = TaskForm()
    
    context = {"tasks": Task.objects.order_by('-pub_date'), "form": form}
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task_text = form.cleaned_data['task_text']
            task = Task(task_text=task_text)
            task.save()
            return HttpResponseRedirect(reverse('to_do:index'), context)
    
    return render(request, 'to_do/index.html', context=context)


def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('to_do:index'))
    
