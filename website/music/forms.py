from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # This places asteriks as password characters are entered

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
