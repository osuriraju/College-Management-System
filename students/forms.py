from django.forms import ModelForm
from .models import Class, Faculty, Student

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'


class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'