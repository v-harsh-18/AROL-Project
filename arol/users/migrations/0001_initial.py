# Generated by Django 4.0.4 on 2022-10-11 09:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=255,
                 primary_key=True, serialize=False, verbose_name='Email')),
                ('full_name', models.CharField(blank=True,
                 max_length=255, verbose_name='Full Name')),
                ('is_active', models.BooleanField(
                    default=True, verbose_name='Is Active')),
                ('is_admin', models.BooleanField(
                    default=False, verbose_name='Is Admin')),
                ('is_staff', models.BooleanField(
                    default=False, verbose_name='Is Staff')),
                ('is_superuser', models.BooleanField(
                    default=False, verbose_name='Is SuperUser')),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='Joined On')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                 related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                 related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'ordering': ['date_joined'],
            },
        ),
    ]
