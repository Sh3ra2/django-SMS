# Generated by Django 5.0 on 2023-12-27 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0008_useradminmodel_descrip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('User Admin', 'User Admin'), ('Student', 'Student'), ('Staff', 'Staff')], max_length=40),
        ),
    ]
