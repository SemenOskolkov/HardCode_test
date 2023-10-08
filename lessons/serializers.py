from rest_framework import serializers
from lessons.models import LessonView


class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = ['lesson', 'user', 'status', 'start_time', 'end_time']
        