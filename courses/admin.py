from django.contrib import admin
from .models import Course, Lesson, UserProgress


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'level', 'price']
    list_filter = ['language', 'level']
    search_fields = ['title']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']
    list_filter = ['course']


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'completed']


from .models import Comment, Like

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'created_at']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson']