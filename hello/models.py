from django.db import models


class User(models.Model):
    login = models.CharField(max_length=30, verbose_name='Логин')
    description = models.TextField(verbose_name='Описание')
    name = models.CharField(max_length=30, verbose_name='Имя')
    email = models.EmailField(max_length=60, verbose_name='E-mail')
    url = models.URLField(verbose_name='URL')
    # password =

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"


class UsersDog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=30, verbose_name='Имя')
    breed = models.CharField(max_length=30, verbose_name='Порода')
    is_bought = models.BooleanField(verbose_name='Дворовая')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Собака"
        verbose_name_plural="Собаки"
        ordering = ['name']
