from django.contrib import admin

# Register your models here.
from lessonview.models import Viewing


@admin.register(Viewing)
class AdminViewing(admin.ModelAdmin):
    pass




