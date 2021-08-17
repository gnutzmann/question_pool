import datetime

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=False)
    question = models.TextField(null=False)
    expected_answer = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category.name + " " + self.question[:50]

    def was_updated_recently(self):
        return self.updated_at >= (timezone.now() - datetime.timedelta(days=1))
