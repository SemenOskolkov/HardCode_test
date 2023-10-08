from rest_framework import serializers
from django.db.models import Sum

from products.models import Product
from users.models import User


class ProductStatisticsSerializer(serializers.ModelSerializer):
    total_views = serializers.SerializerMethodField()
    total_duration = serializers.SerializerMethodField()
    total_users = serializers.SerializerMethodField()
    purchase_percentage = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('id', 
                  'name', 
                  'owner',
                  'total_views',
                  'total_duratio',
                  'total_users',
                  'purchase_percentage',
        )
    
    def get_total_views(self, product):
        '''Рассчет общего количества просмотров уроков для данного продукта'''
        return product.lessonview_set.filter(status='viewed').count()

    def get_total_duration(self, product):
        '''Рассчет суммарной длительности просмотра уроков для данного продукта'''
        return product.lessonview_set.filter(status='viewed').aggregate(total_duration=Sum('lesson__viewing_duration'))['total_duration'] or 0

    def get_total_users(self, product):
        '''Рассчет количества учеников, занимающихся данным продуктом'''
        return product.productaccess_set.count()

    def get_purchase_percentage(self, product):
        '''Рассчет процента приобретения продукта'''
        total_users = User.objects.count()
        if total_users > 0:
            return (product.productaccess_set.count() / total_users) * 100
        return 0
