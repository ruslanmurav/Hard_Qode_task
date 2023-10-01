from django.contrib import admin

# Register your models here.
from lesson.models import Lesson, ProductLesson


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    pass

@admin.register(ProductLesson)
class AdminProductLesson(admin.ModelAdmin):
    pass