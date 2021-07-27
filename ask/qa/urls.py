from django.urls import path, include
from django.contrib import admin
import qa.urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('question/<int:id>/', views.single_question, name='single_question'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular_questions_list, name='popular_questions'),
    path('new/', views.new_questions_list, name='new_questions'),
    path('create/', views.create, name='create')
]
