from django.urls import path
import user_experience.views as views


urlpatterns = [
path("",views.home_view,name='home'),
path("searching/",views.searching_view,name='searching'),
path("user_account_profile/<user_id>",views.user_account_profile_view,name='user_account_profile'),
]