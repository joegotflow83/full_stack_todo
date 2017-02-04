from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    name = models.CharField(max_length=64)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    about_me = models.CharField(max_length=1024, blank=True, null=True)
    friends = models.ManyToManyField(Friend, blank=True)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    due_date = models.DateField()
    created = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
