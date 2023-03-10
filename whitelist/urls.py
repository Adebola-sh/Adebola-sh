from django.urls import path
from whitelist import views

urlpatterns = [
    path('', views.wl, name='wl_form'),
    path('success', views.success, name= 'success'),

]