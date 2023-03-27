from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.create_user),
    path('users/<int:id>/projects/', views.create_project),
    path('users/<int:id>/projectslist/', views.user_project_list),
    path('users/<int:id>/projects/<int:pid>/notes/', views.create_note),
    path('users/<int:id>/projects/<int:pid>/noteslist/', views.project_note_list),
    path('users/<int:id>/projects/<int:pid>/notes/<int:nid>/', views.note_update),
    path('users/<str:username>/<str:password>/', views.get_user_id),
    path('users/<int:id>/projects/<int:pid>/', views.delete_project),
    path('users/<int:id>/projects/<int:pid>/notes/<int:nid>/', views.delete_note),
]