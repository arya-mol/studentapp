from student.models import *
from django.forms import ModelForm
from django import forms

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets={
            "student_name":forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            # "school_name": forms.TextInput(attrs={"class": "form-control"})

        }


class SchoolForm(ModelForm):
    class Meta:
        model=School
        fields="__all__"
        widgets={
            "school_name":forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"})

        }