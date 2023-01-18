from django.urls import path
from . import views
from .views import login_view,teacher_login_view


urlpatterns = [
    path('student/register/', views.student_registration, name='student_registration'),
    path('student/login/', login_view, name='login'),
    path('teacher/register/', views.teacher_registration, name='teacher_registration'),
    path('teacher/login/', teacher_login_view, name='login'),
    ]