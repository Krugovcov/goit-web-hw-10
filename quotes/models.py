from pathlib import Path
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born_date = models.DateField(default=None, null=True, blank=True)  # Замінив DateTimeField на DateField
    born_location = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)  # Краще використати TextField для опису

    def __str__(self):
        return self.fullname


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')
    tags = models.ManyToManyField(Tag, related_name='quotes')

    def __str__(self):
        return f'"{self.text}" - {self.author.fullname}'
