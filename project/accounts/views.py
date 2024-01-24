from django.shortcuts import render


def loginView(request):
    data = {
        'page': 'LogIn',
        'title': 'LogIn User',
        'text': 'Name',
    }
    return render(request, 'accounts/login.html', data)


def logoutView(request):
    data = {
        'page': 'LogOut',
        'title': 'LogOut User',
        'text': 'Name',
    }
    return render(request, 'accounts/login.html', data)
