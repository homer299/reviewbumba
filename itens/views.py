from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import datetime



def iten_view(request):
    return render(request,'itens/iten_page.html')
