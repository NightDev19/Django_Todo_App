from django.db import models

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='todo_images/', null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
