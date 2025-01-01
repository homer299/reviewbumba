from django.urls import path
import shop_account.views as views


urlpatterns = [
path("shop_page/",views.shop_page_view,name='shop_page'),
]