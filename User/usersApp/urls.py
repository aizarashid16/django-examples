from django.urls import path
from usersApp import views
urlpatterns =[
path("",views.Users, name='Users')
]
