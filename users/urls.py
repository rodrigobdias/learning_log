"""Define padrões de URL para users"""

from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
	# Página de login.
    path(r'login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # Página de logout
    path(r'logout/', views.logout_view, name='logout'),
    # Página de cadastro
    path(r'register/', views.register, name='register'),
]






