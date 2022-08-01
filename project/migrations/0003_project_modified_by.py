# Generated by Django 4.0.6 on 2022-08-01 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0002_projectcontribution_modified_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_project_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
