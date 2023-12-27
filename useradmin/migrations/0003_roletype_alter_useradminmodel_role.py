# Generated by Django 5.0 on 2023-12-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0002_alter_useradminmodel_im'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('User Admin', 'User Admin'), ('Student', 'Student'), ('Staff', 'Staff')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='useradminmodel',
            name='role',
            field=models.CharField(choices=[('User Admin', 'User Admin'), ('Student', 'Student'), ('Staff', 'Staff')], max_length=50),
        ),
    ]
