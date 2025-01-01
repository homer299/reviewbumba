from django.urls import path
import itens.views as views


urlpatterns = [
path("iten/",views.iten_view,name='iten_page'),
]