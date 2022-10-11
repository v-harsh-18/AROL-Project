# Generated by Django 4.0.4 on 2022-10-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_Year',
            fields=[
                ('academic_year', models.CharField(max_length=255,
                 primary_key=True, serialize=False, verbose_name='Academic_Year')),
                ('year', models.IntegerField(verbose_name='Year')),
            ],
            options={
                'verbose_name': 'Academic Year',
                'verbose_name_plural': 'Academic Years',
                'ordering': ['academic_year'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category', models.CharField(max_length=255,
                 primary_key=True, serialize=False, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('gender', models.CharField(max_length=255,
                 primary_key=True, serialize=False, verbose_name='Gender')),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
                'ordering': ['gender'],
            },
        ),
        migrations.CreateModel(
            name='Marital_Status',
            fields=[
                ('marital_status', models.CharField(max_length=255,
                 primary_key=True, serialize=False, verbose_name='Marital Status')),
            ],
            options={
                'verbose_name': 'Marital Status',
                'verbose_name_plural': 'Marital Status',
                'ordering': ['marital_status'],
            },
        ),
        migrations.CreateModel(
            name='Qualifying_Exam',
            fields=[
                ('qualifying_exam', models.CharField(max_length=255,
                 primary_key=True, serialize=False, verbose_name='Qualifying Exam')),
            ],
            options={
                'verbose_name': 'Qualifying Exam',
                'verbose_name_plural': 'Qualifying Exams',
                'ordering': ['qualifying_exam'],
            },
        ),
        migrations.CreateModel(
            name='Work_Type',
            fields=[
                ('work_type', models.CharField(max_length=255,
                 primary_key=True, serialize=False, verbose_name='Work Type')),
            ],
            options={
                'verbose_name': 'Work Type',
                'verbose_name_plural': 'Work Types',
                'ordering': ['work_type'],
            },
        ),
    ]
