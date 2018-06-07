from django.conf.urls import url, include
# from django.contrib import admin

# 碰到错误提示, alt + 回车
from django.views.static import serve
import xadmin
from tmall import settings

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    # 商品模块
    url('shop/', include('apps.shop.urls')),
    # 访问media下的所有资源
    url('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
