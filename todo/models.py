from django.db import models
from django import forms


class Categori(models.Model):

    name = models.CharField(max_length=30, unique=True)
    detail = models.TextField()
    owner = models.ForeignKey('auth.User', related_name="categories", on_delete=models.CASCADE)


    def __str__(self) :
        return self.name


class Task(models.Model):

    priorities = (
        ("High","1"),
        ("Medium","2"),
        ("Low","3"),
    )

    title = models.CharField(max_length=100, blank=False)
    explanation = models.TextField()
    categories = models.ManyToManyField("Categori")
    priority = models.CharField(max_length=6, choices=priorities, default="Medium")
    deadline = models.DateField(blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name="tasks", on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title
