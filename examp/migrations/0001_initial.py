# Generated by Django 4.1.1 on 2023-04-21 04:29

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0005_alter_lessons_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('about', models.TextField()),
                ('time', models.PositiveIntegerField(null=True, verbose_name='Vaqt')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lsn', to='course.lessons')),
            ],
        ),
        migrations.CreateModel(
            name='Quizess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Quizs', max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('examp', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='examp.examp')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_update', models.DateTimeField(auto_now=True)),
                ('technique', models.IntegerField(choices=[(0, 'Multiple choice')], default=0)),
                ('title', models.CharField(max_length=123)),
                ('difficulty', models.IntegerField(choices=[(0, 'Fundamental'), (1, 'Beginer'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert')], default=0, verbose_name='Difficulty')),
                ('deta_craeted', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='Active status')),
                ('quizes', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='question', to='examp.quizess')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_update', models.DateTimeField(auto_now=True)),
                ('answer_text', models.CharField(max_length=221, verbose_name='Answer Text')),
                ('is_right', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer', to='examp.question')),
            ],
            options={
                'verbose_name': 'Ansver',
                'ordering': ['id'],
            },
        ),
    ]
