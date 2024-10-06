from django.urls import path
from . import views

app_name = 'task4'

urlpatterns = [
    # post views
    path('platform/', views.platform_view, name='platform_view'),
    path('games/', views.games_view, name='games_view'),
    path('cart/', views.cart_view, name='cart_view'),
    path('test/', views.test),
    path('menu/', views.menu),
]
