from django.urls import path
from . import views
urlpatterns = [
    path('getid/<str:username>/<str:password>/',views.GetUserId.as_view()),
    path('createuser/',views.CreateUser.as_view()),
    path('users/<int:id>/projects/create/',views.CreateProject.as_view()),
    path('users/<int:id>',views.UserProjectList.as_view()),
    path('users/<int:id>/projects/<int:pid>/notes/create',views.CreateNote.as_view()),
    path('users/<int:id>/projects/<int:pid>/notes/',views.ProjectNoteList.as_view()),
    path('users/<int:id>/projects/<int:pid>/notes/<int:nid>/update/',views.NoteUpdate.as_view())
]
