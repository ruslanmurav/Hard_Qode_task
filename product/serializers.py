from rest_framework import serializers

from lesson.models import Lesson
from lessonview.models import Viewing
from product.models import Product, Access


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'owner']


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'


class UserLessonSerializer(serializers.ModelSerializer):
    duration_watching = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_duration_watching(self, obj):
        viewing = Viewing.objects.filter(lesson=obj).first()
        if viewing is None:
            return None
        return viewing.duration

    def get_status(self, obj):
        viewing = Viewing.objects.filter(lesson=obj).first()
        if viewing is None:
            return None
        if viewing.viewed:
            return "Просмотрено"
        else:
            return "Не просмотрено"

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'link', 'duration', 'duration_watching', 'status']



