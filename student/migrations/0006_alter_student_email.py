# Generated by Django 3.2 on 2022-08-17 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
