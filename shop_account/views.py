from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

'''
from shop_account.models import ShopModel
from shop_account.forms import ShopForm
'''

import json



def shop_page_view(request):
    return render(request,'shop_account/shop_page.html')


'''
def create_shop_account_view(request):
    if request.method == "POST":
        print(request.POST.dict())
        return redirect('create_shop_account')
    return render(request,'shop_account/create_shop_account.html')
'''