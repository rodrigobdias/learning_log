"""Define padrões de URL para learning_logs."""

from django.urls import path, re_path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    # Mostra todos os assuntos
    path(r'topics/', views.topics, name='topics'),
    # Página de detalhes para um único assunto
    re_path(r'^topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
    # Página para adicionar um novo assunto
    path(r'new_topic/', views.new_topic, name='new_topic'),
    # Página para adicionar uma nova entrada
    re_path(r'^new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
    # Página para editar uma entrada
    re_path(r'^edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),
]