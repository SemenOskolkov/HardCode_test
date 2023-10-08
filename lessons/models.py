from django.db import models



class Lesson(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')
    video_link = models.URLField(verbose_name='Ссылка на видео')
    viewing_duration = models.IntegerField(verbose_name='Длительность просмотра')
    products = models.ManyToManyField('products.Product', verbose_name='Продукты')
    
    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return f'{self.name} {self.video_link} {self.viewing_duration} {self.products}'
    
    
class LessonView(models.Model):
    VIEWED = 'viewed'
    NOT_VIEWED = 'not_viewed'
    
    STATUS = (
        ('viewed', 'Просмотрено'),
        ('not_viewed', 'Не просмотрено')
    )
    
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE, verbose_name='Урок')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    start_time = models.DateTimeField(verbose_name='Время начала просмотра')
    end_time = models.DateTimeField(verbose_name='Время окончания просмотра')
    status = models.CharField(max_length=20, choices=STATUS, default=NOT_VIEWED, verbose_name='Статус просмотра')
    
    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return f'{self.lesson} {self.user} {self.status}' 
