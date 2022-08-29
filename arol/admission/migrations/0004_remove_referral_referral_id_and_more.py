# Generated by Django 4.0.4 on 2022-08-29 17:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_alter_recommendation_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referral',
            name='referral_id',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='referral_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Referral ID'),
        ),
    ]
