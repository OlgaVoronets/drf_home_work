from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from materials.models import Course, Lesson
from materials.validators import url_validator


class CourseSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели курса"""

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели урока"""
    url = serializers.URLField(validators=[url_validator])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра информации о курсе, включает в себя поля количества уроков и
    списка уроков этого курса"""
    lessons_count = SerializerMethodField()
    lessons_list = SerializerMethodField()

    @staticmethod
    def get_lessons_count(course):
        return Lesson.objects.filter(course=course).count()

    @staticmethod
    def get_lessons_list(course):
        return LessonSerializer(Lesson.objects.filter(course=course), many=True).data

    class Meta:
        model = Course
        fields = '__all__'


class LessonDetailSerializer(serializers.ModelSerializer):
    """Cериализатор для просмотра информации об уроке, где для курса выводится его наименование"""
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'
