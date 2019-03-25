from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    email = forms.EmailField()
