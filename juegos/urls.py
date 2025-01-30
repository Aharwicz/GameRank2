from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Developer
    path('developers/', views.developer_list, name='developer_list'),
    path('developers/<int:pk>/rank/', views.rank_developer, name='rank_developer'),  # Ruta para puntuar developers
    path('developers/add/', views.developer_add, name='developer_add'),
    path('developers/<int:pk>/edit/', views.developer_edit, name='developer_edit'),
    path('developers/<int:pk>/delete/', views.developer_delete, name='developer_delete'),

    # Rutas para Publisher
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('publishers/<int:pk>/rank/', views.rank_publisher, name='rank_publisher'),  # Ruta para puntuar publishers
    path('publishers/add/', views.publisher_add, name='publisher_add'),
    path('publishers/<int:pk>/edit/', views.publisher_edit, name='publisher_edit'),
    path('publishers/<int:pk>/delete/', views.publisher_delete, name='publisher_delete'),

    # Rutas para Juego
    path('juegos/', views.juego_list, name='juego_list'),
    path('juegos/<int:pk>/rank/', views.rank_juego, name='rank_juego'),  # Ruta para puntuar juegos
    path('juegos/add/', views.juego_add, name='juego_add'),
    path('juegos/<int:pk>/edit/', views.juego_edit, name='juego_edit'),
    path('juegos/<int:pk>/delete/', views.juego_delete, name='juego_delete'),
]
