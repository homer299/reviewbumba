from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from user_account.forms import UserAccoutRegistrationForm#, AccountAuthenticationForm, AccountUpdateForm
from user_account.models import UserAccount



def UserAccountRegistrationView(request, *args, **kwargs):
    context = {}
    if request.POST:
        form = UserAccoutRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            print(email)
            print(raw_password)
            return redirect('home')
        else:
            context['registration_form'] = form

    else:
        form = UserAccoutRegistrationForm()
        context['registration_form'] = form
    return render(request, 'user_account/create_user_account.html', context)