from django.urls import path
import shop_account.views as views


urlpatterns = [
path("shop_page/",views.shop_page_view,name='shop_page'),
#path("create_shop_account/",views.create_shop_account_view,name='create_shop_account'),
]