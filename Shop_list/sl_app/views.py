from django.http import HttpResponse
from django.template import loader
from sl_app.models import User_to_list, Shop_list
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def slist(request):
    if request.method == 'GET':
        lst = User_to_list.objects.get(user_id=1).list_id
        shoplst = Shop_list.objects.filter(list_id=lst, status= 'нужно купить').values()
        template = loader.get_template('shop_list.html')
        context = {
            'shoplst': shoplst
        }
        return HttpResponse(template.render(context, request))

def add(request):
    return HttpResponse('Добавление продукта')

def buy(request, item_id):
    return HttpResponse('Покупка')

def remove(request, item_id):
    return HttpResponse('Удаление из списка')
