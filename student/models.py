from django.db import models

# Create your models here.


class School(models.Model):
    school_name=models.CharField(max_length=120,unique=True)
    email=models.EmailField(unique=True,null=True)

    def __str__(self):
        return self.school_name


class Student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=120)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=120)

    def __str__(self):
        return self.school_name