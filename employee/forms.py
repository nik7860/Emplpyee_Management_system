from django import forms
from .models import employeedetail
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employeedetail
        fields = '__all__' 
    class Meta:
        model = User
        fields = '__all__'