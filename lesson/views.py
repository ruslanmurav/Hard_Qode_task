from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from lesson.models import Lesson
from lesson.serializers import LessonSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
