from django.shortcuts import render

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
    return render(request, 'shop_detail.html', {'msg': 'success'})


# 用户id
def shop_car(request):
    cars = ShopCar.objects.filter(user_id=1)
    for car in cars:
        car.shop.images = car.shop.shopimage_set.filter(type='type_single').first()
    return render(request, 'shop_car.html', {'cars': cars})
