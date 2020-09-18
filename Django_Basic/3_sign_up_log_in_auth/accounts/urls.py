from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('', views.accounts, name="accounts"),
    path('userpage', views.userpage, name='userpage'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),

]
