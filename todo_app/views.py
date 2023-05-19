from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'  
    context_object_name = 'tasks'  

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'  
    context_object_name = 'task'  

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    fields = ['author', 'title', 'task_case', 'image_task', 'status']
    success_url = reverse_lazy('tasks:task-list')
    
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_update.html'
    fields = ['author', 'title', 'task_case', 'image_task', 'status']

    def get_success_url(self):
        return reverse_lazy('tasks:task-detail', kwargs={'pk': self.object.pk})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'  # Шлях до вашого шаблону підтвердження видалення завдання
    success_url = reverse_lazy('tasks:task-list')