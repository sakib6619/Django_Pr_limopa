from django.urls import path
from .views import login,register,logout,forgotten
urlpatterns = [
    path('login/',login, name='login'),
    path('register/',register, name='register'),
    path('logout/',logout, name='logout'),
    path('forgotten /',forgotten, name='forgotten'),
]