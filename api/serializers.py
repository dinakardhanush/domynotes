from rest_framework import serializers
from  . import models
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    class Meta:
        model = models.UserModel
        fields = ['id','username','password']

class ProjectSerializer(serializers.ModelSerializer):
    projectname = serializers.CharField(required=True)
    #user = UserSerializer(read_only=True)
    class Meta:
        model = models.ProjectModel
        fields=['id','projectname']


class NoteSerializer(serializers.ModelSerializer):
    notename = serializers.CharField(required=True)
    content=serializers.CharField()
    #project = ProjectSerializer(read_only=True)
    class Meta:
        model = models.NoteModel
        fields=['id','notename','content']


class IdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields=['id']