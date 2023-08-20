from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Note, MyUser


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            "title",
            "content",
        )
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter title"}),
            "content": forms.TextInput(attrs={"placeholder": "Enter content"}),
        }


class UserCreateForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username",)
        # widgets = {"password": forms.PasswordInput}


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "id": "inputUsername", "class": "input"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "input", "id": "inputPw"}
        )
    )
