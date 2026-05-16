from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('paid', 'Оплачен'),
        ('cancelled', 'Отменён'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        unique_together = ['user', 'course']

    def __str__(self):
        return f'{self.user.username} — {self.course.title}'