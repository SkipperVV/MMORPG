from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

CATEGORY = ['Танки', 'Хилы', 'ДД', 'Торговцы', 'Гилдмастеры', 'Квестгиверы', 'Кузнецы', 'Кожевники', 'Зельевары', 'Заклинатели']

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text=_("Выбор геймера"))
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.user}'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text=_("Введите название новой категории"))
    subscribers = models.ManyToManyField(User, related_name='categories')#для обращения через user.categories.all
    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, help_text=_("Выбор автора"))
    post_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField('Заголовок', max_length=100, help_text=_("Введите заголовок"))
    text = models.TextField('Содержание', default='Введите техт', help_text=_("Содержание статьи"))
    # post_type = models.CharField(max_length=20, choices=CATEGORY, default='Танки')
    category = models.ManyToManyField(Category, through='PostCategory')

    def __str__(self):
        return f"{self.title}"

class PostCategory(models.Model):  # OneToMany
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)