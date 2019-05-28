from django import forms
from .models import Student, Grade


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class GradeForm(forms.ModelForm):

    class Meta:
        model = Grade
        exclude = ('student',)
