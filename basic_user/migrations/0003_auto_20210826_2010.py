# Generated by Django 3.1.7 on 2021-08-26 10:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic_data', '0001_initial'),
        ('basic_user', '0002_alter_profile_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='basic_data.city', verbose_name='город'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city_to_move',
            field=models.ManyToManyField(blank=True, related_name='city_to_move', to='basic_data.City', verbose_name='города для переезда'),
        ),
        migrations.AddField(
            model_name='profile',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания'),
        ),
        migrations.AddField(
            model_name='profile',
            name='desired_position',
            field=models.ManyToManyField(blank=True, related_name='desired_position', to='basic_data.Profession', verbose_name='желаемые профессии'),
        ),
        migrations.AddField(
            model_name='profile',
            name='desired_salary',
            field=models.IntegerField(blank=True, null=True, verbose_name='желаемая зарплата'),
        ),
        migrations.AddField(
            model_name='profile',
            name='desired_skill',
            field=models.ManyToManyField(blank=True, related_name='desired_skills', to='basic_data.Skill', verbose_name='желаемые навыки'),
        ),
        migrations.AddField(
            model_name='profile',
            name='disability_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='basic_data.disabilitygroup', verbose_name='группа инвалидности'),
        ),
        migrations.AddField(
            model_name='profile',
            name='dysfunctions_body',
            field=models.ManyToManyField(blank=True, to='basic_data.DysfunctionBody', verbose_name='физические ограничения'),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.ManyToManyField(blank=True, to='basic_data.Education', verbose_name='образование'),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='адрес'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.ManyToManyField(blank=True, related_name='profession', to='basic_data.Profession', verbose_name='профессии по образованию'),
        ),
        migrations.AddField(
            model_name='profile',
            name='restrictions_categories_life',
            field=models.ManyToManyField(blank=True, to='basic_data.RestrictionCategoriesLife', verbose_name='ограничение категорий жизнедеятельности'),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='skills', to='basic_data.Skill', verbose_name='компетенции'),
        ),
        migrations.AddField(
            model_name='profile',
            name='work_experience',
            field=models.ManyToManyField(blank=True, related_name='work_experience', to='basic_data.Profession', verbose_name='опыт работы'),
        ),
    ]
