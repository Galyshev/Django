import uuid

from django.http import HttpResponse, HttpResponseNotFound
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
            return redirect('/user/authorization')

def logaut(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/user/authorization')
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
        email = request.POST.get("email")
        user = User.objects.create_user(username, email, password)
        user.save()
        list_id = uuid.uuid4()
        user_to_list = User_to_list(user_id=user.id, list_id=list_id, or_list=list_id)
        user_to_list.save()
        return redirect('/user/authorization')
def invite(request):
    if request.method == 'GET':
        template = loader.get_template('invite.html')
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        email = request.POST.get("email")
        invate_user = User.objects.filter(email=email).first()
        if invate_user is None:
            return HttpResponseNotFound('Пользователь не найден')

        current_user_list = User_to_list.objects.get(user_id=request.user.id).list_id
        User_to_list.objects.filter(user_id=invate_user.id).update(list_id=current_user_list)
        template = loader.get_template('invite_ok.html')
        context = {'name': invate_user.username}
        return HttpResponse(template.render(context, request))

def remove_user(request):
    if request.method == 'GET':
        template = loader.get_template('remove.html')
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        email = request.POST.get("email")
        invate_user = User.objects.filter(email=email).first()
        if invate_user is None:
            return HttpResponse('Пользователь не найден')

        original_user_list = User_to_list.objects.get(user_id=invate_user.id).or_list
        User_to_list.objects.filter(user_id=invate_user.id).update(list_id=original_user_list)
        template = loader.get_template('remove_ok.html')
        context = {'name': invate_user.username}
        return HttpResponse(template.render(context, request))

def add_shop(request):
    if request.method == 'GET':
        template = loader.get_template('add_mall.html')
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        user_id = request.user.id
        lst = User_to_list.objects.get(user_id=user_id).list_id
        mall = request.POST.get("name_mall")
        save_mall = MallList(name_mall=mall, list_id=lst)
        save_mall.save()
        return redirect('/user/add_item')

def add_item(request):
    if request.method == 'GET':
        user_id = request.user.id
        lst = User_to_list.objects.get(user_id=user_id).list_id
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
