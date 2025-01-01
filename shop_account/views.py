from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import datetime



def shop_page_view(request):
    return render(request,'shop_account/shop_page.html')
