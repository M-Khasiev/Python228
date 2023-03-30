from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
]

