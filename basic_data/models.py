from django.db import models


class City(models.Model):
    """Таблица городов"""
    name = models.CharField('название города', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'


class Skill(models.Model):
    """Таблица навыков"""
    name = models.CharField('название ключевого навыка', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'skill'


class Education(models.Model):
    """Таблица образования"""
    name = models.CharField('образование', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'education'



class WorkExperience(models.Model):
    """Таблица опыта работы"""
    name = models.CharField('опыт работы', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'work_experience'


class EmploymentType(models.Model):
    """Таблица типов занятости"""
    name = models.CharField('тип занятости', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employment_type'


class Schedule(models.Model):
    """Таблица графиков работы"""
    name = models.CharField('график работы', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'schedule'


class DysfunctionBody(models.Model):
    """Таблица нарушений функций организма"""
    name = models.CharField('вид нарушения функций организма', max_length=200)
    description = models.TextField('описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'dysfunction_body'


class RestrictionCategoriesLife(models.Model):
    """Таблица ограничений основных категорий жизнедеятельности"""
    name = models.CharField('ограничения основных категорий жизнедеятельности', max_length=200)
    description = models.TextField('описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'restriction_category_life'


class DisabilityGroup(models.Model):
    """Таблица групп инвалидностей"""
    name = models.CharField('группа инвалидности', max_length=200)
    description = models.TextField('описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'disability_group'


class Profession(models.Model):
    """Таблица профессий"""
    def contact_default():
        return ""

    name = models.CharField('название профессии', max_length=200)
    boundProfession = models.ManyToManyField('self', blank=True, verbose_name='связанные профессии')
    description = models.TextField('описание профессии', default=contact_default)
    education = models.ManyToManyField(Education, blank=True)
    dysfunctionBody = models.ManyToManyField(DysfunctionBody,  blank=True, verbose_name='связанный вид нарушения функций организма')
    restrictionCategoriesLife = models.ManyToManyField(RestrictionCategoriesLife,  blank=True, verbose_name='связанный ограничения основных категорий жизнедеятельности')
    disabilityGroup = models.ManyToManyField(DisabilityGroup,  blank=True, verbose_name='связанная группа инвалидности')
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'profession'
