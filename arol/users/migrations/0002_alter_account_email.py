# Generated by Django 4.0.4 on 2022-08-24 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(db_index=True, max_length=255, primary_key=True, serialize=False, verbose_name='Email'),
        ),
    ]
