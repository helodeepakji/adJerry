
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('sign_in',views.sign_in,name='sign_in'),
    path('sign_up',views.sign_up,name='sign_up'),
]
