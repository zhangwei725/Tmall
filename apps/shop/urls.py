from django.conf.urls import url
from apps.shop import views

urlpatterns = [
    url('index/', views.index, name='index'),
    url('search/', views.search),
    url('cate/', views.cate),
    url('detail/(\d+)/', views.shop_detail, name='detail')
]
