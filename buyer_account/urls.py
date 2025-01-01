from django.urls import path
import buyer_account.views as views


urlpatterns = [
path("profile/",views.buyer_profile_view,name='profile_page'),
]