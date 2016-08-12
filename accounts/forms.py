from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        if commit:
            user.save()
        return user
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
        'username': '아이디를 입력하세요',
        'password1': '비밀번호를 입력하세요.',
        'password2': '비밀번호를 한번 더 입력하세요.'
        }