from django.db import models
from django.contrib.auth.models import User
from basic_user.models import Profile
from basic_data.models import Profession
from django.utils.timezone import now


class Course(models.Model):
    """Таблица кусов созданных унивеситетом"""

    def contact_default():
        return ""

    name = models.CharField('Название образовательной программы', max_length=200, default=contact_default)
    profession = models.ForeignKey(Profession, verbose_name='Компетенция', on_delete=models.PROTECT, null=True)
    description = models.TextField('Описание образовательной программы', default=contact_default)
    count = models.IntegerField(verbose_name='Количество мест', null=True)
    price = models.IntegerField(verbose_name='Стоимость обучения на 1 человека', null=True)
    profiles = models.ManyToManyField(Profile, verbose_name='Ученики', blank=True, related_name='profile')
    confirmed_profile = models.ManyToManyField(Profile, verbose_name='Подтвержденные ученики', blank=True, related_name='confirmed_profile')
    created_time = models.DateTimeField('дата создания', default=now)
    last_mod_time = models.DateTimeField('дата последнего изменения', default=now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course'


class Univer(models.Model):
    """"Таблица университетов"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('Наименование университета', max_length=200)
    course = models.ManyToManyField(Course, verbose_name='Курсы', blank=True)
    created_time = models.DateTimeField('дата создания', default=now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'univer'