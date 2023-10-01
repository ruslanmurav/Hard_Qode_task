from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from lesson.models import Lesson


class Viewing(models.Model):
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()
    viewed = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        data = super(Viewing, self).save()
        threshold = 0.8 * self.lesson.duration

        if self.duration >= threshold:
            self.viewed = True
            super().save(update_fields=['viewed'])

