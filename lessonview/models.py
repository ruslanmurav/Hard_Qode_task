from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from lesson.models import Lesson


class Viewing(models.Model):
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()
    viewed = models.BooleanField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    