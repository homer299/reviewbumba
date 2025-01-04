from django.urls import path
import user_account.views as views


urlpatterns = [
path("create_user_account/",views.UserAccountRegistrationView,name='create_user_account'),
]