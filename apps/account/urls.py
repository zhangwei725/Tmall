from django.conf.urls import url

from apps.account import views

urlpatterns = [
    url('login/', views.login, name='login'),
    url('register/', views.register, name='register'),
    url('logout/', views.register, name='loginout'),
]
