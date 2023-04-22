# Generated by Django 4.1.1 on 2023-04-12 11:33

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_lessons_files_alter_file_fille_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
    ]