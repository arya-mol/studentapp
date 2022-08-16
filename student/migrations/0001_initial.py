# Generated by Django 3.2 on 2022-08-16 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('department', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.school')),
            ],
        ),
    ]