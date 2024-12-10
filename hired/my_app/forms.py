from django import forms
from .models import JobApplication
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job_title', 'company_name', 'status', 'job_link', 'job_description', 'notes', 'attachments']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')