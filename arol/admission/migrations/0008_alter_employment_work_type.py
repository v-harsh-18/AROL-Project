# Generated by Django 4.0.4 on 2022-05-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0007_alter_qualifying_examination_options_recommendation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='work_type',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Temporary', 'Temporary'), ('Permanent', 'Permanent'), ('Contract', 'Contract')], max_length=255, verbose_name='Type of Work'),
        ),
    ]
