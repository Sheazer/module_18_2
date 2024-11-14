from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['Erzhan', 'Volodya', 'Davis', 'Ashot']


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            info['name'] = form.cleaned_data['username']
            info['password'] = form.cleaned_data['password']
            info['repeat_password'] = form.cleaned_data['repeat_password']
            info['age'] = form.cleaned_data['age']
            if info['password'] != info['repeat_password']:
                info['error'] = 'Пароли не совпадают!'
                return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})
            elif info['name'] in users:
                info['error'] = 'Такой пользователь существует!'
                return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})
            elif int(info['age']) < 18:
                info['error'] = 'Вы должны быть старше 18!'
                return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})
            else:
                info['error'] = 'Success'
                return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info, 'username': info['name']})
            # print(name)
            # print(password)
            # print(repeat_password)
            # print(age)
    else:
        form = UserRegister()
        info['error'] = 'Empty'
        print('Failed==============================>')
    return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})


