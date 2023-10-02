from django.db.models import Sum
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


class UserProductSerializer(serializers.ModelSerializer):
    duration_watching = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    last_watching = serializers.SerializerMethodField()

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

    def get_last_watching(self, obj):
        viewing = Viewing.objects.filter(lesson=obj).first()

        if viewing is None:
            return None
        return viewing.last_watching

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'link', 'duration', 'duration_watching', 'status', 'last_watching']


class StatisticsSerializer(serializers.ModelSerializer):
    count_watched = serializers.SerializerMethodField()
    total_viewing = serializers.SerializerMethodField()

    def get_count_watched(self, obj):
        viewings = Viewing.objects.filter(lesson__productlesson__product=obj)
        total_views = viewings.count()
        return total_views

    def get_total_viewing(self, obj):
        viewings = Viewing.objects.filter(lesson__productlesson__product=obj)
        total_duration = 0

        for viewing in viewings:
            total_duration += viewing.duration
        return total_duration

    class Meta:
        model = Product
        fields = ['id', 'name', 'owner', 'count_watched', 'total_viewing']



