# Generated by Django 3.1.7 on 2021-08-26 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import university.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basic_user', '0003_auto_20210826_2010'),
        ('basic_data', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=university.models.Course.contact_default, max_length=200, verbose_name='Название образовательной программы')),
                ('description', models.TextField(default=university.models.Course.contact_default, verbose_name='Описание образовательной программы')),
                ('count', models.IntegerField(null=True, verbose_name='Количество мест')),
                ('price', models.IntegerField(null=True, verbose_name='Стоимость обучения на 1 человека')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата последнего изменения')),
                ('confirmed_profile', models.ManyToManyField(blank=True, related_name='confirmed_profile', to='basic_user.Profile', verbose_name='Подтвержденные ученики')),
                ('profession', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='basic_data.profession', verbose_name='Компетенция')),
                ('profiles', models.ManyToManyField(blank=True, related_name='profile', to='basic_user.Profile', verbose_name='Ученики')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Univer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование университета')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания')),
                ('course', models.ManyToManyField(blank=True, to='university.Course', verbose_name='Курсы')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'univer',
            },
        ),
    ]