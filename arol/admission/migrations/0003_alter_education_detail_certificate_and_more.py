# Generated by Django 4.0.4 on 2022-06-07 18:21

import admission.models.education
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education_detail',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to=admission.models.education.upload_certificate, verbose_name='Certificate'),
        ),
        migrations.AlterField(
            model_name='education_detail',
            name='marksheet',
            field=models.FileField(blank=True, null=True, upload_to=admission.models.education.upload_marksheet, verbose_name='Marksheet'),
        ),
        migrations.AlterField(
            model_name='education_detail',
            name='percent',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Percent or CPI/CGPA'),
        ),
    ]