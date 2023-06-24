from django.urls import path

from . import views
from .views import (
    GameshopApiCheck,
    GameshopApiGamesView,
    GameshopApiCategoriesView,
    GameshopApiDevelopersView,
    GameshopApiAddDeveloper,
    GameshopApiManageDeveloper,
    GameshopApiAddCategory,
    GameshopApiManageCategory
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
    path('api/', GameshopApiCheck.as_view()),
    path('api/games/', GameshopApiGamesView.as_view()),
    path('api/developers/', GameshopApiDevelopersView.as_view()),
    path('api/categories/', GameshopApiCategoriesView.as_view()),
    path('api/admin/developers/', GameshopApiAddDeveloper.as_view()),
    path('api/admin/developers/<int:pk>', GameshopApiManageDeveloper.as_view()),
    path('api/admin/category/', GameshopApiAddCategory.as_view()),
    path('api/admin/category/<int:pk>', GameshopApiManageCategory.as_view())
]