from django.shortcuts import render

# Create your views here.
def platform_view(request):
    return render(request, 'third_task/platform.html')


items = [
    ['https://ru.wikipedia.org/wiki/Hexen', 'Hexen'],
    ['https://ru.wikipedia.org/wiki/Diablo_(серия_игр)', 'Diablo'],
    ['https://ru.wikipedia.org/wiki/Half-Life_(серия_игр)', 'Half-Life'],
    ['https://ru.wikipedia.org/wiki/Need_for_Speed', 'Need For Speed'],
    ['https://www.zoneofgames.ru/games/', 'Новинки'],
]
def games_view(request):
    return render(request, 'third_task/games.html', context={'items': items,})

orders = [
    ['Заказ 1', 10, 'б/у'],
    ['Заказ 2', 17800, 'отличное'],
    ['Заказ 3', 310, 'хорошее'],
    ['Заказ 4', 100, 'хорошее'],
]
orders_cnt = len(orders)
# orders_cnt = 0
total = sum([order[1] for order in orders])

def cart_view(request):
    return render(request, 'third_task/cart.html',
                  context={'orders': orders, 'total': total, 'orders_cnt': orders_cnt})

