from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('lesson/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('my-courses/', views.my_courses, name='my_courses'),
]