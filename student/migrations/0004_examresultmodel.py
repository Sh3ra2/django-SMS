# Generated by Django 5.0 on 2023-12-18 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_examsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='examresultmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField()),
                ('obtained_marks', models.IntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.examsmodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentmodel')),
            ],
        ),
    ]