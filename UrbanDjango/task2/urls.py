from django.urls import path
from . import views

app_name = 'task2'

urlpatterns = [
    # post views
    path('class/', views.class_view, name='class_view'),
    path('func/', views.func_view, name='func_view'),
]

