from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from sl_app.models import User_to_list, MallList, Item
from django.template import loader
from django.contrib.auth import logout, authenticate, login


def authorization(request):
    if request.method == 'GET':
        template = loader.get_template('authorization.html')
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        username = request.POST.get("login")
        password = request.POST.get("psw")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/shop_list')

        else:
            return redirect('/authorization')

def logaut(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/shop_list/')
    else:
        return HttpResponse("Вы не авторизованы")


def register(request):
    if request.method == 'GET':
        template = loader.get_template('register.html')
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        username = request.POST.get("login")
        password = request.POST.get("psw")
        user = User.objects.create_user(username, '', password)
        user.save()
        return redirect('/shop_list')

def add_shop(request):
    return HttpResponse('Добавление магазина')

def add_item(request):
    if request.method == 'GET':
        lst = User_to_list.objects.get(user_id=1).list_id
        mall = MallList.objects.filter(list_id=lst).values()

        return render(request, 'add_item.html', {'mall': mall})
    else:
        name_item = request.POST.get("name_item")
        mall_id_chk = int(request.POST.get("mall"))
        item = Item(name_item=name_item, shop_id_id=mall_id_chk)
        item.save()

        return redirect('/shop_list/slist')
def analytics(request):
    return HttpResponse('Расходы за месяц')
