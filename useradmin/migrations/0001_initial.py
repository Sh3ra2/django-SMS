# Generated by Django 5.0 on 2023-12-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='useradminmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('im', models.ImageField(upload_to=None)),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=50)),
                ('role', models.CharField(choices=[('P', 'Principle'), ('C', 'Clerk'), ('O', 'Other')], max_length=50)),
                ('join_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
