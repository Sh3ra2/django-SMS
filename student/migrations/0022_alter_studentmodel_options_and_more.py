# Generated by Django 5.0 on 2023-12-27 11:34

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0015_remove_staffmodel_address_and_more'),
        ('student', '0021_remove_examsmodel_studentforexam'),
        ('useradmin', '0010_delete_roletype_alter_useradminmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentmodel',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterModelManagers(
            name='studentmodel',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='examsmodel',
            name='studentforexam',
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='user_type',
        ),
        migrations.RemoveField(
            model_name='subjectpapermodel',
            name='pstudent',
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='admitted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.staffmodel'),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='customuser_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='useradmin.customuser'),
            preserve_default=False,
        ),
    ]
