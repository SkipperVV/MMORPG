from django.shortcuts import render


def PostsView(request):
    data = {
        'page': 'Публикации',
        'title': 'Заголовок статьи',
        'text': 'текст, внутри которого могут быть картинки, встроенные видео и другой контент.',
    }
    return render(request, 'posts/posts_home.html', data)
