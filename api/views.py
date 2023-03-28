from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from . import models, serializers


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    username = request.data.get('username')
    if models.UserModel.objects.filter(username=username).exists():
        return Response({'error': 'UAE'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = serializers.UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_project(request, id):
    try:
        user = models.UserModel.objects.get(pk=id)
    except models.UserModel.DoesNotExist:
        return Response({'error': 'UDNE'}, status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.ProjectSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def user_project_list(request, id):
    projects = models.ProjectModel.objects.filter(user=id)
    serializer = serializers.ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_note(request, id, pid):
    try:
        user = models.UserModel.objects.get(id=id)
    except models.UserModel.DoesNotExist:
        raise ValidationError("Invalid user ID")

    try:
        project = models.ProjectModel.objects.get(id=pid, user=user)
    except models.ProjectModel.DoesNotExist:
        raise ValidationError("Invalid project ID")

    serializer = serializers.NoteSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(project=project)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def project_note_list(request, id, pid):
    notes = models.NoteModel.objects.filter(project__user=id, project_id=pid)
    serializer = serializers.NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def note_update(request, id, pid, nid):
    try:
        note = models.NoteModel.objects.get(project__user=id, project_id=pid, id=nid)
    except models.NoteModel.DoesNotExist:
        raise ValidationError('Note does not exist.')

    serializer = serializers.NoteSerializer(note, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_id(request, username, password):
    queryset = models.UserModel.objects.filter(Q(username=username) & Q(password=password))
    serializer = serializers.IdSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])

def delete_project(request, id, pid):
    try:
        project = models.ProjectModel.objects.get(id=pid, user=id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except models.ProjectModel.DoesNotExist:
        return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_note(request, id, pid, nid):
    try:
        note = models.NoteModel.objects.get(id=nid, project__user_id=id, project_id=pid)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except models.NoteModel.DoesNotExist:
        return Response({"error": "Note not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def search_notes(request, id, pid, notename):
    try:
        notes = models.NoteModel.objects.filter(
            project__user=id,
            project_id=pid,
            notename__icontains=notename,
        )
        serializer = serializers.NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except models.ProjectModel.DoesNotExist:
        return Response({'error': 'Project not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)