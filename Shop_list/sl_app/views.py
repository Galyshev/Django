import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse

from sl_app.models import User_to_list, Shop_list, MallList, Item

def index(request):
    if request.user.is_authenticated:
        return redirect('/shop_list/slist')
    else:
        return redirect('/user/authorization')

def slist(request):
    if request.method == 'GET':
        lst = User_to_list.objects.get(user_id=1).list_id
        sql = '''
                select * from sl_app_shop_list 
                join sl_app_item
                on sl_app_shop_list.item_id_id = sl_app_item.id
                join sl_app_malllist
                on sl_app_malllist.id = sl_app_item.shop_id_id
                where sl_app_shop_list.list_id = %s
                and sl_app_shop_list.status = "нужно купить";
                '''
        shoplst = Shop_list.objects.raw(sql, [str(lst), ])
        current_user = User.objects.get(username=request.user.username)
        print(current_user)
        template = loader.get_template('shop_list.html')
        context = {
            'shoplst': shoplst,
            'current_user': current_user
        }
        return HttpResponse(template.render(context, request))


def add_to_list(request):
    if request.method == 'GET':
        lst = User_to_list.objects.get(user_id=1).list_id
        mall = MallList.objects.filter(list_id=lst).values()
        template = loader.get_template('choice_mall.html')
        context = {
            'mall': mall,
        }
        return HttpResponse(template.render(context, request))

    else:
        mall_chk = request.POST.get("mall")
        mall_name = MallList.objects.get(id=mall_chk).name_mall
        print(mall_name)
        item = Item.objects.filter(shop_id_id=mall_chk).values()
        request.session['mall_chk'] = mall_chk
        return redirect('/shop_list/add_ok')


def add_ok(request):
    if request.method == 'GET':
        mall_chk = request.session.get('mall_chk', '')
        mall_name = MallList.objects.get(id=mall_chk).name_mall
        item = Item.objects.filter(shop_id_id=mall_chk).values()
        template = loader.get_template('add_item_to_sList.html')
        context = {
            'mall_name': mall_name,
            'item': item
        }
        return HttpResponse(template.render(context, request))
    else:
        quantity = request.POST.get("quantity")
        item_id = request.POST.get("item")
        date = request.POST.get("date")
        print(quantity, item_id, date)
        lst = User_to_list.objects.get(user_id=1).list_id
        new_row = Shop_list(list_id=lst, quantity=quantity, price=0.00, status='нужно купить', buy_date=date, item_id_id=item_id)
        new_row.save()
        return redirect('/shop_list/slist')



def buy(request, id, name_item):
    name_item = str(name_item).replace('>', '')
    id = str(id).replace('<', '')
    if request.method == 'GET':
        template = loader.get_template('buy_item.html')
        context = {
            'name_item': name_item,
        }
        return HttpResponse(template.render(context, request))
    else:
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        date = datetime.datetime.now().date()
        Shop_list.objects.filter(id=id).update(quantity=quantity, price=price, status='куплено', buy_date=date)
        return redirect('/shop_list/slist')

def del_from_list(request, id):
    id = str(id).replace('<', '').replace('>', '')
    date = datetime.datetime.now().date()
    Shop_list.objects.filter(id=id).update( status='отмена', buy_date=date)
    return redirect('/shop_list/slist')

def remove(request, item_id):
    return HttpResponse('Удаление из списка')


# return redirect('/shop_list/slist')