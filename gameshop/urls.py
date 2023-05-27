from django.urls import path

from . import views

app_name = 'gameshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('regulamin/', views.regulamin, name='regulamin'),
    path('pomoc/', views.pomoc, name='pomoc'),
]