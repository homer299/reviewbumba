from django.urls import path
import user_account.views as views


urlpatterns = [
path("create_user_account/",views.UserAccountRegistrationView,name='create_user_account'),
path("login_user_account/",views.UserAccountLoginView,name='login_user_account'),
path("logout_user_account/",views.UserAccountLogoutView,name='logout_user_account'),

]