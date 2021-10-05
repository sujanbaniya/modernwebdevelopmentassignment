from django import forms
from froala_editor.widgets import FroalaEditor
from django.contrib.auth.forms import UserCreationForm
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['content']


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user