from rest_framework import generics
from lessons.models import LessonView

from lessons.serializers import LessonViewSerializer


class LessonListView(generics.ListAPIView):
    serializer_class = LessonViewSerializer
    
    def get_queryset(self):
        user = self.request.user
        return LessonView.objects.filter(user=user)
