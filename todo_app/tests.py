from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task

class TaskCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_task(self):
        url = reverse('tasks:task-create')
        data = {
            'author': self.user.id,
            'title': 'Test Task',
            'task_case': 'This is a test task',
            'status': 'OPEN'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) 
        task = Task.objects.latest('id')
        self.assertEqual(task.title, 'Test Task') 
    
        self.assertRedirects(response, reverse('tasks:task-list'))