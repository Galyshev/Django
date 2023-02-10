from django.http import HttpResponse
from django.shortcuts import render


from sl_app.models import User_to_list, MallList, Item
from django.template import loader

def authorization(request):
    if request.method == 'GET':
        template = loader.get_template('authorization.html')
        return HttpResponse(template.render())
    else:
        return "Coming soon"

def register(request):
    return HttpResponse('Регистрация. Будет реализована позже')

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

        return render(request, 'index.html')
def analytics(request):
    return HttpResponse('Расходы за месяц')
