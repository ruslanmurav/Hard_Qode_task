from django.db import models

# Create your models here.
from product.models import Product


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    duration = models.PositiveIntegerField()


class ProductLesson(models.Model):
    product = models.ForeignKey(to=Product)
    Lesson = models.ForeignKey(to=Lesson)

