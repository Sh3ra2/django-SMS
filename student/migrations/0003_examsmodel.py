# Generated by Django 5.0 on 2023-12-18 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_alter_staffmodel_im'),
        ('student', '0002_rename_admitted_by_studentmodel_admitted_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='examsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=80)),
                ('subject_name', models.CharField(max_length=80)),
                ('invigilator', models.ManyToManyField(to='staff.staffmodel')),
                ('taken_by', models.ManyToManyField(to='student.studentmodel')),
            ],
        ),
    ]
