# Generated by Django 4.1.7 on 2023-03-27 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_projectmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('notename', models.CharField(max_length=300)),
                ('content', models.TextField(max_length=500)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.projectmodel')),
            ],
        ),
    ]
