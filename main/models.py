from django.db import models

# Create your models here.
class TaskModel(models.Model):
    
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle