import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.shop.models import ShopCar, Shop

'''
1> 选择商品 加入购物车
2> 

'''


def add_car(request):
    try:
        num = request.GET.get('num')
        shop_id = request.GET.get('shop_id')
        shop = Shop.objects.get(pk=int(shop_id))
        if 0 < int(num) < shop.stock:
            ShopCar.objects.create(number=int(num), shop_id=int(shop_id), user_id=1)
    except:
        pass
    return render(request, '', {'msg': 'success'})


#  自定义的过滤器
"""
1>在app中创建templatetags文件
2>在templatetags中创建一个自定义过滤器的py文件
2.1>导包
2.2>实例化注册对象
2.3> 定义函数(过滤器)
    @register.filter
    @register.simple_tag
3>在模板中{% load 过滤器文件名 %}
4>使用 
    
"""


# 用户id
def shop_car(request):
    user_id = request.session.get('userinfo').get('uid')
    if user_id:
        cars = ShopCar.objects.filter(user_id=user_id, status=1)
        for car in cars:
            car.shop.image = car.shop.shopimage_set.filter(type='type_single').first()
    return render(request, 'cart1.html', {'cars': cars})


# 数组  列表
# 对象  字典
def buy_shop(request):
    if request.method == 'POST':
        # 获取用户提交的数据
        cars = request.POST.get('cars')
        cars = json.loads(cars)
        for car in cars:
            num = car['num']
            car_id = car['car_id']
            ShopCar.objects.filter(car_id=car_id).update(number=num, status=2)
    return redirect('http://127.0.0.1:8000/car/confirm')


def confirm_buy_shop(request):
    user_id = request.session.get('userinfo').get('uid')
    if user_id:
        cars = ShopCar.objects.filter(user_id=user_id, status=2)
        for car in cars:
            car.shop.image = car.shop.shopimage_set.filter(type='type_single').first()
    return render(request, 'buy_page.html', {'cars': cars})
