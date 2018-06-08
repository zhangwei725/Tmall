import datetime
import json

from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

"""
创建自定义的apps
1.通过命令创建模块   startapp app_name
2.配置二级路由
2.1> 在apps下面新建一个urls.py文件
2.2> 在根目录的urls.py中使用include引入
注意:
如果项目比较大的,最好是在apps下面新建一个templates的文件夹
1>根目录的templates文件夹一般放一些公共的模板文件 母版 需要include的模板


配置项目后台管理
1> 导入xamdin 
2> 在setting中添加xamin项目 sys.path.insert(0,os.path.join(BASE_DIR,'xadmin'))
3> 导入xadmin需要的依赖包
3.1> 需要安装第三方的app   requirements
3.2> 通过命令  pip install requirements(如果已经安装可以跳过)
3.3> 先将xadmin下面的requirements.txt文件复制到工程中
3.4> 通过命令   pip install -r  目录/xxx.txt
     例如: pip install -r requirements/xadmin.txt
3.5 通过  pip list 查看是否安装成功

4> 注册
    # 必须
    'xadmin',
    'crispy_forms',
    # 可选
    # 扩展主题包
    'reversion'
5> 解决冲突
5.1> 在根目录在新建一个ext_apps
5.2> 将xmadin的源代码 赋值到 ext_apps下面
5.3> 将ext_apps 加入到项目 sys.path.insert(0, os.path.join(BASE_DIR, 'ext_apps'))

6> 使用xadmin代替django admin  
    在根urls.py中 
     url('xadmin/', xadmin.site.urls), 
7 系统表迁移
1> makemigrations
2> migrations

8>创建超级用户
python manage.py createsuperuser

9> 启动项目测试是否安装成功
9.1> http://127.0.0.1:8000/xadmin/
9.2> 使用第8步的账号密码登录

MTV开发
1>在models中建立模型对象
2>迁移
t
v
"""

# 数据库迁移出现问题
'''
1> django_migrations  表里的每一条对应一个app下的每次生产一个对应文件
'''
from .models import Navigation, Category, Banner, Shop, Property, PropertyValue, Review


#
def index(request):
    navigations = Navigation.objects.all()
    # 查询一级分类菜单数据
    cate_list = Category.objects.all()
    # 动态语言 可以动态的添加属性
    for cate in cate_list:
        # 获取二级菜单的数据
        submenus = cate.submenu_set.all()
        for menu in submenus:
            # 将二级菜单对象的多条三级菜单数据绑定到 subs2属性
            menu.subs2 = menu.submenu2_set.all()
        cate.subs = submenus
        # 商品信息
        shops = cate.shop_set.all()
        for shop in shops:
            shop.images = shop.shopimage_set.all()
        cate.shops = shops

    # 获取轮播图的数据
    banners = Banner.objects.all()

    # 获取商品信息
    # cate_shops = Category.objects.all()
    # for cate in cate_shops:
    #     shops = cate.shop_set.all()
    #     for shop in shops:
    #         shop.images = shop.shopimage_set.all()
    #     cate.shops = shops
    return render(request, 'index.html', {'navigations': navigations,
                                          'cate_list': cate_list,
                                          'banners': banners,
                                          })


"""
{
status:200,
msg :sucess',
data:cate_list
}
#json {} 对应python的字典
#json [] 对应python的列表
# 支持基本类型  bool  数字  None  字符串

python不支持对象转化json  

"""


def cate(request):
    result = {}
    # 需要把对象转化字典
    cates = Category.objects.all()
    cate_list = []
    # 对象要转化成字典 cate-----> 字典
    for cate in cates:
        menus = cate.submenu_set.all()  # QS
        li = []
        # 将二级菜单的数据转化字典  submenu--->字典
        for menu in menus:
            li2 = []
            for menu2 in menu.submenu2_set.all():
                li2.append(model_to_dict(menu2))
            menu.subs2 = li2
            li.append(model_to_dict(menu))
        cate.subs = li
        cate_list.append(model_to_dict(cate))

    result.update(status=200, msg='success', data=cate_list)
    return HttpResponse(json.dumps(result), content_type='application/json')

    """
    前后端分离
    用户请求服务器的静态文件(不经过)---> 浏览器开始解析html css js
    ---->当浏览器js的ajax
     ---->(客服端发送ajax请求)
    --->views接口--->
    返回响应的数据(json数据)
    --->解析
    --->dom操作
    --->显示给用户

    前后端不分离
    浏览器访问服务器的资源路径 ---
    views(从数据库拿数据---->
    给模板)-->
    渲染--->
    显示给用户
    """
    # key: value
    # 属性 = 值
    # 把对象转化字典


def model_to_dict(model):
    # vars(对象)获取对象所有的属性
    dic = {}
    keys = vars(model).keys()
    for key in keys:
        if not key.startswith('_'):
            if isinstance(getattr(model, key), datetime.date):
                getattr(model, key).strtime('%Y-%m-%d')
            elif isinstance(getattr(model, key), datetime.datetime):
                dic[key] = getattr(model, key).strtime('%Y-%m-%d %H%m%s')
            else:
                # getattr(key) 获取属性的值
                dic[key] = getattr(model, key)
    return dic


def shop_detail(request, sid):
    shop = Shop.objects.get(pk=int(sid))
    shop.imgs = shop.shopimage_set.all()
    # 通过分类菜单获取商品的参数
    properties = Property.objects.filter(cate_id=shop.cate.cate_id)
    for property in properties:
        # 获取商品的参数通过shop_id 商品 propertyvalue
        property.value = PropertyValue.objects.get(property_id=716)
    # 获取商品的评论信息
    reviews = Review.objects.filter(shop_id=147)
    return render(request, 'shop_detail.html', {'shop': shop, 'properties': properties, 'reviews': reviews})


"""
1>使用form表单
2>location.href
3>使用重定向技术
"""


# render
# render  url地址不会发生改变 本界面的刷新 TemplateResponse
# redirect url地址会发生改变  相当于两次请求 可以是所有的地址

# ?key=value

# def search(request):
#     key = request.GET.get('keyword')
#     return redirect(reverse('search1', args=(key,)))

def search(request):
    key = request.GET.get('keyword')
    shops = Shop.objects.filter(name__icontains=key)
    for shop in shops:
        # select  * from  shop_img  where type='type_single'
        shop.images = shop.shopimage_set.filter(type='type_single').values('shop_img_id', 'shop_id')
        shop.count = shop.review_set.count()
    return render(request, 'search.html', {'shops': shops})
