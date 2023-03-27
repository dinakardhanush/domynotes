from django.http import HttpResponse
from rest_framework import generics,status
from . import models
from rest_framework.response import Response
from . import serializers
from rest_framework.exceptions import ValidationError
from django.db.models import Q
# Create your views here.

class CreateUser(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        if models.UserModel.objects.filter(username=username).exists():
            return Response({'error': 'UAE'}, status=status.HTTP_400_BAD_REQUEST)
            
        return super().create(request, *args, **kwargs)   

class CreateProject(generics.CreateAPIView):
    serializer_class = serializers.ProjectSerializer

    def create(self, request, *args, **kwargs):
        user_id = self.kwargs.get('id')
        try:
            user = models.UserModel.objects.get(pk=user_id)
        except models.UserModel.DoesNotExist:
            return Response({'error': 'UDNE'}, status=status.HTTP_404_NOT_FOUND)
        

        user = models.UserModel.objects.get(pk=user_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserProjectList(generics.ListAPIView):
    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('id')
        return models.ProjectModel.objects.filter(user=user_id)
    

class CreateNote(generics.CreateAPIView):
    serializer_class = serializers.NoteSerializer
  
    def perform_create(self, serializer):
        user_id = self.kwargs.get('id')
        project_id = self.kwargs.get('pid')

        try:
            user = models.UserModel.objects.get(id=user_id)
        except models.UserModel.DoesNotExist:
            raise ValidationError("Invalid user ID")

        try:
            project = models.ProjectModel.objects.get(id=project_id, user=user)
        except models.ProjectModel.DoesNotExist:
            raise ValidationError("Invalid project ID")

        serializer.save(project=project)

    def get_queryset(self):
        user_id = self.kwargs.get('id')
        project_id = self.kwargs.get('pid')
        return models.NoteModel.objects.filter(project_id=project_id, project__user_id=user_id)
    

class ProjectNoteList(generics.ListAPIView):
    serializer_class = serializers.NoteSerializer

    def get_queryset(self):
        user = self.kwargs.get('id')
        project_id = self.kwargs.get('pid')
        return models.NoteModel.objects.filter(project__user=user, project_id=project_id)
    
class NoteUpdate(generics.UpdateAPIView):
    serializer_class = serializers.NoteSerializer


    def get_object(self):
        try:
            user = self.kwargs.get('id')
            project_id = self.kwargs.get('pid')
            note_id = self.kwargs.get('nid')
            note = models.NoteModel.objects.get(project__user=user, project_id=project_id, id=note_id)
            return note
        except models.NoteModel.DoesNotExist:
            raise ValidationError('Note does not exist.')
        


class GetUserId(generics.ListAPIView):
    serializer_class = serializers.IdSerializer

    def get_queryset(self):
        #username = self.request.query_params.get('username') can also be used
        username = self.kwargs.get('username')
        password = self.kwargs.get('password')
        queryset = models.UserModel.objects.filter(username=username, password=password)
        return queryset

