from django.urls import path

from . import views
from .views import (
    GameshopApiGeneralView
)

app_name = 'gameshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('regulamin/', views.regulamin, name='regulamin'),
    path('pomoc/', views.pomoc, name='pomoc'),
    path('login/', views.userlogin, name='login'),
    path('register/', views.register, name='register'),
    path('game/<slug:slug>/',views.game, name='game'),
    path('logout/', views.userlogout, name='logout'),
    path('otpa/', views.otpa, name='otpa'),
    path('api', GameshopApiGeneralView.as_view())
]