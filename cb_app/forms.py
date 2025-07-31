from django import forms
from .models import Student




class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Full Name',
            'age': 'Age',
            'email': 'Email Address',
            'address': 'Home Address',
        }
        help_texts = {
            'name': 'Enter the full name of the student.',
            'age': 'Enter the age in years.',
            'email': 'Enter a valid email address.',
            'address': 'Enter the home address of the student.',
        }
        
