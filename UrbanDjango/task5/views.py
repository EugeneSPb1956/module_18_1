from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister


# Create your views here.
users = [
    {'username': 'User1',
     'password': 'abcdefgh',
     'age': 19},
    {'username': 'User2',
     'password': '12345678',
     'age': 40},
    {'username': 'User3',
     'password': 'abracadabra',
     'age': 109},
]
info = {'user': ''}


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            # проверка наличия пользователя в users[]
            user_exists = False
            for user in users:
                if user['username'] == username:
                    user_exists = True
                    print('Такой пользавтель уже есть')
                    break
            if password == repeat_password and age >= 18 and not user_exists:
                users.append({'username': username,
                              'password': password,
                              'age': age})
                return render(request, 'fifth_task/registration_page.html', {'user': f'Приветствуем, {username}!'})
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'fifth_task/registration_page.html', context=info)
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'fifth_task/registration_page.html', context=info)
            elif user_exists:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'fifth_task/registration_page.html', context=info)
            else:
                print('Неизвестная ошибка')
                info['error'] = 'Неизвестная ошибка'
                return render(request, 'fifth_task/registration_page.html', context=info)
    else:
        form = UserRegister()
        return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        # проверка наличия пользователя в users[]
        user_exists = False
        for user in users:
            if user['username'] == username:
                user_exists = True
                print('Такой пользавтель уже есть')
                break
        if password == repeat_password and age >= 18 and not user_exists:
            users.append({'username': username,
                          'password': password,
                          'age': age})
            return render(request, 'fifth_task/registration_page.html', {'user': f'Приветствуем, {username}!'})
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'fifth_task/registration_page.html', context=info)
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'fifth_task/registration_page.html', context=info)
        elif user_exists:
            info['error'] = 'Пользователь уже существует'
            return render(request, 'fifth_task/registration_page.html', context=info)
        else:
            print('Неизвестная ошибка')
    else:
        return render(request, 'fifth_task/registration_page.html', {'user': ''})
