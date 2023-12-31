# Generated by Django 5.0 on 2023-12-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('staff', '0010_alter_staffmodel_managers_staffmodel_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staffmodel',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='staff_user_groups', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='staff_user_permissions', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
