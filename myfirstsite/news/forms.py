from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import re

from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(
                attrs={'class': 'form-control'},
            )
        }


    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'^\s*\d', title):
            raise ValidationError("Заголовок не должен начинаться из цифры")
        return title


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    email = forms.CharField(
        label="Email",
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
