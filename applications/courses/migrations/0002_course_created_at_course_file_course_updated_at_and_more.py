# Generated by Django 5.1 on 2024-08-29 10:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='course',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='course/files'),
        ),
        migrations.AddField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='course/videos'),
        ),
    ]