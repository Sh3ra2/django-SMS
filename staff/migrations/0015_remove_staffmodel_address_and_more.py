# Generated by Django 5.0 on 2023-12-27 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0014_remove_staffmodel_address_and_more'),
        ('useradmin', '0010_delete_roletype_alter_useradminmodel_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffmodel',
            name='address',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='password',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='user_type',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='username',
        ),
        migrations.AddField(
            model_name='staffmodel',
            name='customuser_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='useradmin.customuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='added_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='useradmin.useradminmodel'),
        ),
    ]