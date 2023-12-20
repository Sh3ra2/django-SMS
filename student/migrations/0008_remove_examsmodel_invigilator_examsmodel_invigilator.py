# Generated by Django 5.0 on 2023-12-20 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_alter_staffmodel_options'),
        ('student', '0007_examsmodel_selected_class_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examsmodel',
            name='invigilator',
        ),
        migrations.AddField(
            model_name='examsmodel',
            name='invigilator',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='staff.staffmodel'),
        ),
    ]
