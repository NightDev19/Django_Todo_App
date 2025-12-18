from django.db import models
import os

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='todo_images/', null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
