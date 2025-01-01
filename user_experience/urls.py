from django.urls import path
import user_experience.views as views


urlpatterns = [
path("",views.home_view,name='home'),
path("searching/",views.searching_view,name='searching'),
]