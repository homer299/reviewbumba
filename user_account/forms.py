from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from user_account.models import UserAccount


class UserAccoutRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')

    class Meta:
        model = UserAccount
        fields = ('email', 'username', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = UserAccount.objects.exclude(pk=self.instance.pk).get(email=email)
        except UserAccount.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = UserAccount.objects.exclude(pk=self.instance.pk).get(username=username)
        except UserAccount.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)