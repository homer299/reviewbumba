from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import datetime



def home_view(request):
    return render(request,'user_experience/home.html')


def searching_view(request):
    return render(request,'user_experience/searching.html')
