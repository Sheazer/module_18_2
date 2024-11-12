from django.shortcuts import render


def main_template(request):
    title = 'Учебный портал'
    head = 'Главная страница'
    main = 'Главная'
    courses = 'Курсы'
    profile = 'Мой профиль'
    context = {
        'title': title,
        'head': head,
        'main': main,
        'courses': courses,
        'profile': profile,
    }
    return render(request, 'fourth_task/main.html', context)


def courses(request):
    title = 'Курсы'
    head = 'Мои курсы'
    courses = ['Python', 'Java', 'C++']
    home = 'Главная страница'
    context = {
        'title': title,
        'head': head,
        'courses': courses,
        'home': home,
    }
    return render(request, 'fourth_task/courses.html', context)


def profile(request):
    title = 'Мой профиль'
    head = 'Мои данные'
    name = 'Erzhan'
    age = '21.03.2003'
    star = 'good'
    context = {
        'title': title,
        'head': head,
        'name': name,
        'age': age,
        'star': star,
        'home': 'Главная страница',
    }

    return render(request, 'fourth_task/profile.html', context)
