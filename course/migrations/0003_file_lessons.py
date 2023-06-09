# Generated by Django 4.1.1 on 2023-04-10 11:04

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_rename_deegre_teacher_degree'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=41)),
                ('fille', models.FileField(upload_to='ph_cours/')),
            ],
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=61)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('about', models.TextField()),
                ('video', models.FileField(upload_to='vid_cours/')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='course.course')),
                ('files', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='course.file')),
            ],
        ),
    ]
