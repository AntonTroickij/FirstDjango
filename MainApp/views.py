from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist
 
 
# items = [
#      {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#      {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#      {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#      {"id": 7, "name": "Картофель фри" ,"quantity":0},
#      {"id": 8, "name": "Кепка" ,"quantity":124},
#  ]
 
 
def home(request):
     context = {
         "name": "Петров Иван Николаевич",
         "email": "my_mail@mail.ru"
     }
     return render(request, "index.html", context)
 
def about(request):
     author = {
     "name": "Иван",
     "middle_name": "Петрович",
     "last_name": "Иванов",
     "phone": "8-923-600-01-02",
     "email": "vasya@mail.ru"
     }
     return render(request, "about.html", {"author": author})
 
 
def get_item(request, item_id: int):
    ''' По указанному id возвращаем элемент из БД'''
    try:
        item = Item.objects.get(id=item_id)
        colors = []
        # Проверяем что у элемента есть хоть один цвет
        if item.colors.exists():
            colors = item.colors.all()
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Item with id={item_id} not found")
    else:
        context = {
            "item": item,
            "colors": colors,
            }
        return render(request, "item_page.html", context)

 
 
def get_items(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)