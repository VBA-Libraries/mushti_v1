# Generated by Django 4.1 on 2022-08-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0006_alter_project_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="project_image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
