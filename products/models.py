from django.db import models


class Product(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец')
    name = models.CharField(max_length=300, verbose_name='Название')
    
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.name} {self.owner}'
    

class ProductAccess(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name='Продукт')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    
    class Meta:
        verbose_name = 'доступ у продукту'
        verbose_name_plural = 'доступы к продуктам'

    def __str__(self):
        return f'{self.product} {self.user}'
