from django.db import models
from django.contrib.auth.models import User
from basic_data.models import City, DisabilityGroup, Education, Profession, \
    DysfunctionBody,  RestrictionCategoriesLife, Skill
from django.utils.timezone import now


class Profile(models.Model):
    """"Таблица пользователей с ОВЗ"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name1 = models.CharField('фамилия', max_length=200, blank=True)
    name2 = models.CharField('имя', max_length=200, blank=True)
    name3 = models.CharField('отчество', max_length=200, blank=True)
    description = models.TextField('кортко о себе', max_length=500, blank=True)
    sex = models.IntegerField('пол', blank=True, default=1)
    birth_date = models.DateField('дата рождения', null=True, blank=True)
    date_creation = models.DateField('дата создания', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name1 = models.CharField('фамилия', max_length=200, blank=True)
    name2 = models.CharField('имя', max_length=200, blank=True)
    name3 = models.CharField('отчество', max_length=200, blank=True)
    description = models.TextField('кортко о себе', max_length=500, blank=True)
    sex = models.IntegerField('пол', blank=True, default=1)
    birth_date = models.DateField('дата рождения', null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, default = 1, verbose_name='город')
    city_to_move = models.ManyToManyField(City, blank=True, related_name='city_to_move', verbose_name='города для переезда')
    location = models.CharField('адрес', max_length=30, default='', blank=True)
    education = models.ManyToManyField(Education, blank=True, verbose_name='образование')
    work_experience = models.ManyToManyField(Profession, blank=True, related_name='work_experience', verbose_name='опыт работы')
    disability_group = models.ForeignKey(DisabilityGroup, verbose_name='группа инвалидности', on_delete=models.PROTECT, blank=True, null=True)
    dysfunctions_body = models.ManyToManyField(DysfunctionBody, blank=True, verbose_name='физические ограничения')
    restrictions_categories_life = models.ManyToManyField(RestrictionCategoriesLife, blank=True, verbose_name='ограничение категорий жизнедеятельности')
    skills = models.ManyToManyField(Skill, blank=True, related_name='skills', verbose_name='компетенции')
    profession = models.ManyToManyField(Profession, blank=True, related_name='profession', verbose_name='профессии по образованию')
    desired_position = models.ManyToManyField(Profession, blank=True, related_name='desired_position', verbose_name='желаемые профессии')
    desired_skill = models.ManyToManyField(Skill, blank=True, related_name='desired_skills', verbose_name='желаемые навыки')
    desired_salary = models.IntegerField(verbose_name='желаемая зарплата', null=True, blank=True)
    created_time = models.DateTimeField('дата создания', default=now)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'profile'

