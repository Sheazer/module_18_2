from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['Erzhan', 'Volodya', 'Davis', 'Ashot']


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            print(name)
            print(password)
            print(repeat_password)
            print(age)
            return HttpResponse('Форма успешно отправлено!')
    else:
        form = UserRegister()
        print('Failed==============================>')
    return render(request, 'fifth_task/registration_page.html', {'form': form})


