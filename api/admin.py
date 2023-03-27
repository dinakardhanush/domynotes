from django.contrib import admin
from . import models
# Register your models here.
class UserAdminShow(admin.ModelAdmin):
    list_display = ['id','username','password']
    class Meta:
        models = models.UserModel
admin.site.register(models.UserModel,UserAdminShow)



class ProjectAdminShow(admin.ModelAdmin):
    list_display = ['id','projectname','user']
    class Meta:
        models = models.ProjectModel
admin.site.register(models.ProjectModel,ProjectAdminShow)


class NoteAdminShow(admin.ModelAdmin):
    list_display = ['id','notename','project']
    class Meta:
        models = models.NoteModel
admin.site.register(models.NoteModel,NoteAdminShow)