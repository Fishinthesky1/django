from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ("OPEN", "Open"),
    ("IN_PROGRESS", "In Progress"),
    ("DONE", "Done"),
]

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("Zagolovok", max_length=80)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    task_case = models.TextField()
    image_task = models.ImageField("", upload_to=None, height_field=None, width_field=None, max_length=None)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
    
