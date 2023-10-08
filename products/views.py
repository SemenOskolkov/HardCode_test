from rest_framework import generics
from lessons.models import LessonView
from lessons.serializers import LessonViewSerializer
from products.models import Product

from products.serializers import ProductStatisticsSerializer


class ProductLessonListView(generics.ListAPIView):
    serializer_class = LessonViewSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        return LessonView.objects.filter(user=user, lesson__products=product_id)


class ProductStatisticsView(generics.ListAPIView):
    serializer_class = ProductStatisticsSerializer
    queryset = Product.objects.all()
