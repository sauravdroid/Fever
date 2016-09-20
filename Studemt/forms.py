from django import forms
from .models import *


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['student', ]


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Hello
        exclude = ['date_time','serial','student']
