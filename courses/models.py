from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Начинающий'),
        ('intermediate', 'Средний'),
        ('advanced', 'Продвинутый'),
    ]
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
    ]

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, verbose_name='Язык')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name='Уровень')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена')
    image_url = models.URLField(blank=True, verbose_name='Картинка')
    stepik_id = models.IntegerField(unique=True, null=True, blank=True, verbose_name='ID на Stepik')
    stepik_url = models.URLField(blank=True, verbose_name='Ссылка на Stepik')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name='Курс')
    title = models.CharField(max_length=200, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    quiz_question = models.TextField(blank=True, verbose_name='Вопрос теста')
    quiz_answer = models.CharField(max_length=200, blank=True, verbose_name='Ответ теста')
    youtube_url = models.URLField(blank=True, verbose_name='YouTube ссылка')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['order']

    def __str__(self):
        return f'{self.course.title} — {self.title}'


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    completed = models.BooleanField(default=False, verbose_name='Пройден')
    completed_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Прогресс'
        verbose_name_plural = 'Прогресс пользователей'
        unique_together = ['user', 'lesson']

    def __str__(self):
        return f'{self.user.username} — {self.lesson.title}'
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='comments', verbose_name='Урок')
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} — {self.lesson.title}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='likes', verbose_name='Урок')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        unique_together = ['user', 'lesson']

    def __str__(self):
        return f'{self.user.username} — {self.lesson.title}'