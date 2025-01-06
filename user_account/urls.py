from django.urls import path
import user_account.views as views
from django.contrib.auth import views as auth_views


urlpatterns = [
path("create_user_account/",views.UserAccountRegistrationView,name='create_user_account'),
path("update_user_account/<user_id>/edit",views.update_user_account_view,name='update_user_account'),
path("login_user_account/",views.UserAccountLoginView,name='login_user_account'),
path("logout_user_account/",views.UserAccountLogoutView,name='logout_user_account'),

#Password Change
path('user_account/password_change/', auth_views.PasswordChangeView.as_view(template_name='user_account/password_change.html'),name='password_change'),

path('user_account/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='user_account/password_change_done.html'), name='password_change_done'),
]