from django.urls import path
from . import views
from django.contrib.auth import views as auth_viwes

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_viwes.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_viwes.LogoutView.as_view(), name='logout'),
]
