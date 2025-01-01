from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import datetime



def buyer_profile_view(request):
    return render(request,'buyer_account/profile_page.html')
