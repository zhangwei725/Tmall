from django.shortcuts import render, redirect

# 登录
from apps.shop.models import User, ShopCar

"""
会话管理
服务器识别客服端的一种技术
cookie 保存服务器发送的数据 存在客服端   
客服端发起请求(如果cookie存在,浏览器自动将cookie信息发送到服务器)
---->服务器端(服务器端获取cookie的信息)
如何获取  request.COOKIE能获取到信息 如果cookie信息不存在
(要么cookie过期,要么第一次访问)

如何设置
1>resp = HttpResponse()
2>resp.set_cookie('key',value)
为了解决cookie不太安全
session  服务器  保存全局的数据  
获取跟设置都是request
request.session[]
request.session.get()

request.session[key]=value
reqeust.setdefault()



























































"""


# cookie
# session
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        # 判断用户名和密码不能为空
        if username and password:
            users = User.objects.filter(name=username)
            if users:
                user = users.first()
                if user.password == password:
                    # 表示登录成功
                    # 查询用户购车的商品数
                    count = user.shopcar_set.count()
                    userinfo = {
                        'uid': user.uid,
                        'name': user.name,
                        'count': count,
                    }
                    request.session['userinfo'] = userinfo
                    return redirect('/shop/index')
                else:
                    return render(request, 'login.html', {'msg': '用户名或密码错误'})
            else:
                # 用户不存在
                return render(request, 'login.html', {'msg': '用户不能存在'})
        else:
            return render(request, 'login.html', {'msg': '用户名或密码不能为空'})
            # 用户密码不能为空
    else:
        return render(request, 'login.html', {'msg': '错误请求方式!'})


def register(request):
    pass


def loginout(request):
    del request.session['userinfo']
    return redirect('/shop/index/')
