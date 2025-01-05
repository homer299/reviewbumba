from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

from django.conf import settings
from user_account.forms import UserAccoutRegistrationForm, UserAccountAuthenticationForm
from user_account.models import UserAccount



def UserAccountRegistrationView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated: 
        return HttpResponse("You are already authenticated as " + str(user.email))
    context = {}
    if request.POST:
        form = UserAccoutRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')

            account = authenticate(email=email, password=raw_password)
            login(request, account)

            print(email)
            print(raw_password)
            print(user)
            return redirect('home')
        else:
            context['registration_form'] = form

    else:
        form = UserAccoutRegistrationForm()
        context['registration_form'] = form
    return render(request, 'user_account/create_user_account.html', context)




def UserAccountLoginView(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated: 
        return redirect("home")

    if request.POST:
        form = UserAccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                print(user)
                return redirect("home")
    else:
        form = UserAccountAuthenticationForm()

    context['login_form'] = form
    return render(request, "user_account/login_user_account.html", context)



def UserAccountLogoutView(request):
    logout(request)
    return redirect("home")