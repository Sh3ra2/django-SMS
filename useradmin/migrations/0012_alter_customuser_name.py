# Generated by Django 5.0 on 2023-12-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0011_alter_customuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, default='CustomUserIns', max_length=50, null=True),
        ),
    ]
