from django.shortcuts import render


def MainView(request):
    data={
        'page': 'Главная страница',
        'title': 'Заглавие главной страницы',
        'text': 'Наполнение главной страницы главной страницыглавной страницыглавной страницыглавной страницыглавной страницы',
    }
    return render(request, 'main/home.html', data)


def AboutView(request):
    data={
        'page': 'О нас',
        'title': 'Заглавие рассказа о себе',
        'text': 'Рассказ о нас, любимых Рассказ о нас, любимых Рассказ о нас, любимых Рассказ о нас, любимых ',
    }
    return render(request, 'main/home.html', data)
    # return render(request, 'main/about.html')
