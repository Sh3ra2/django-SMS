# Generated by Django 5.0 on 2023-12-28 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0016_alter_staffmodel_added_by'),
        ('useradmin', '0010_delete_roletype_alter_useradminmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffmodel',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='useradmin.useradminmodel'),
        ),
    ]
