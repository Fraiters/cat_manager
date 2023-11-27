from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, Textarea, TextInput, PasswordInput, Form
from .models import Cat


class AddCatForm(ModelForm):
    """ Форма добавления кота """
    class Meta:
        model = Cat
        fields = ['name', 'age', 'breed', 'weight', 'photo', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-input'}),
            'description': Textarea(attrs={'cols': 50, 'rows': 10})
        }

    def clean_name(self):
        """ Пользовательская валидация для name"""
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина превышает максимально допустимое число символов (200)')
        return name


class RegisterUserForm(UserCreationForm):
    """ Форма регистрации пользователя """
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))
    password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class': 'form-input'}),
            'password1': PasswordInput(attrs={'class': 'form-input'}),
            'password2': PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginUserForm(AuthenticationForm):
    """ Форма авторизации пользователя """
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))
