from django.conf.urls import url

from apps.car import views

urlpatterns = [
    url('add/', views.add_car, name='add'),
    url('show/', views.shop_car, name='show'),
    url('buy/', views.buy_shop, name='buy'),
]
