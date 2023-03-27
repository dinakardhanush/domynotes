from django.db import models

# Create your models here.

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True,max_length=20)
    password = models.CharField(max_length=30)
    def __str__(self) ->str:
        return str(self.id)+" "+self.username
    

class ProjectModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    projectname = models.CharField(max_length=300)

    def __str__(self) -> str:
        return str(self.id)+" "+self.projectname
    

class NoteModel(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(ProjectModel,on_delete=models.CASCADE)
    notename = models.CharField(max_length=300)
    content = models.TextField(max_length=500)

    def __str__(self) -> str:
        return str(self.id)+" "+self.notename
    

