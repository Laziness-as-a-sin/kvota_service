from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """"Таблица 'Пользователь с ОВЗ'"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name1 = models.CharField('фамилия', max_length=200, blank=True)
    name2 = models.CharField('имя', max_length=200, blank=True)
    name3 = models.CharField('отчество', max_length=200, blank=True)
    description = models.TextField('кортко о себе', max_length=500, blank=True)
    sex = models.IntegerField('пол', blank=True, default=1)
    birth_date = models.DateField('дата рождения', null=True, blank=True)
    date_creation = models.DateField('дата создания', null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'profile'

