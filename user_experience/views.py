from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from user_account.models import UserAccount
import datetime



def home_view(request, *args, **kwargs):
    user = request.user
    print(user)
    return render(request,'user_experience/home.html')


def searching_view(request):
    return render(request,'user_experience/searching.html')


def user_account_profile_view(request, *args, **kwargs):
    context = {}
    user = request.user#Current logged account
    is_self = True
    user_id = kwargs.get("user_id")#Getting user id from the url

    try:
        account = UserAccount.objects.get(pk=user_id)#getting the account with id as in the url(which the profile page belongs to)
        print("=============Got User object by pk/user_id =========")
        print(account)
        print("====================================================")
    except UserAccount.DoesNotExist :
        return HttpResponse("Something went wrong.")

    if user.is_authenticated and user != account or not user.is_authenticated:
        is_self = False
        print("=============Different User/Not Auth=========================")
        print(user.is_authenticated)
        print(user)
        print("=============================================================")


    if account:
        context['id'] = account.id
        context['username'] = account.username
        context['email'] = account.email

        # Set the template variables to the values
        context['is_self'] = is_self
        return render(request, "user_experience/user_account_profile.html", context)