from django.urls import path

from products.apps import ProductsConfig
from products.views import ProductLessonListView, ProductStatisticsView


app_name = ProductsConfig.name


urlpatterns = [
    path('product/<int:product_id>/lessons/', ProductLessonListView.as_view(), name='product_lessons_list'),
    path('products_statistics/', ProductStatisticsView.as_view(), name='products_statistics'),
]