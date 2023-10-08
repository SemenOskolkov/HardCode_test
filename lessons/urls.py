from django.urls import path

from lessons.apps import LessonsConfig
from lessons.views import LessonListView


app_name = LessonsConfig.name


urlpatterns = [
    path('lessons_list/', LessonListView.as_view(), name='lessons_list'),
]
