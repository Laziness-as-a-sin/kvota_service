from django.db import models
from django.contrib.auth.models import User
from basic_data.models import City, Education, Profession, DisabilityGroup, \
    EmploymentType, Schedule, Skill, DysfunctionBody, RestrictionCategoriesLife
from basic_user.models import Profile
from django.utils.timezone import now

class Firm(models.Model):
    """Таблица фирм"""

    def contact_default():
        return ""

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField('название фирмы', max_length=200)
    description = models.TextField('описание фирмы', default=contact_default)
    created_time = models.DateTimeField('дата создания', default=now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'firm'


class WorkPlace(models.Model):
    """Таблица рабочих мест созданных фирмой"""
    def contact_default():
        return ""

    name = models.CharField('Title work place', max_length=200, default=contact_default, blank=True)
    firm = models.ForeignKey(Firm, verbose_name='фирма', on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, verbose_name='город', on_delete=models.PROTECT, default=1)
    location = models.CharField('Адрес', max_length=200, default='Державина 15')
    education = models.ForeignKey(Education, verbose_name='образование', on_delete=models.PROTECT, null=True)
    profession = models.ForeignKey(Profession, verbose_name='профессия', on_delete=models.CASCADE, null=True)
    employment_type = models.ManyToManyField(EmploymentType, verbose_name='тип занятости', blank=True)
    schedule = models.ManyToManyField(Schedule, verbose_name='график работы', blank=True)
    skill = models.ManyToManyField(Skill, verbose_name='компетенции', blank=True)
    dysfunctions_body = models.ManyToManyField(DysfunctionBody, blank=True, verbose_name='физические ограничения')
    restrictions_categories_life = models.ManyToManyField(RestrictionCategoriesLife, blank=True, verbose_name='ограничение категорий жизнедеятельности')
    disability = models.ManyToManyField(DisabilityGroup, verbose_name='ограничения', blank=True)
    min_salary = models.IntegerField(verbose_name='минимальная зарплата', null=True)
    max_salary = models.IntegerField(verbose_name='максимальная зарплата', null=True)
    profile_liked = models.ManyToManyField(Profile, verbose_name="Пользователи лайкнутые работадателем", blank = True, related_name='profile_liked')
    liked_by_profile = models.ManyToManyField(Profile, verbose_name="Пользователи которые лайкнули", blank = True, related_name='liked_by_profile')
    count = models.IntegerField(verbose_name='Количество рабочих мест', default=1)
    created_time = models.DateTimeField('дата создания', default=now)
    last_mod_time = models.DateTimeField('дата последнего изменения', default=now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'work_place'