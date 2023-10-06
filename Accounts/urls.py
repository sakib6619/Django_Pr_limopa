from django.urls import path
from .views import login,register,forgotten
urlpatterns = [
    path('login/',login, name='login'),
    path('register/',register, name='register'),
    path('forgotten /',forgotten, name='forgotten'),
]