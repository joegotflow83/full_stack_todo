from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    due_date = models.DateField()
    created = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
