from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    
    
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
