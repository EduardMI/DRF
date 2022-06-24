from django.db import models

from user_app.models import User


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    url = models.URLField(max_length=128)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.project} - {self.name}'
