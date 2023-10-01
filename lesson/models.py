from django.db import models

# Create your models here.


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    duration = models.PositiveIntegerField()

class
