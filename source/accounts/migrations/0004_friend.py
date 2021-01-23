# Generated by Django 3.1.5 on 2021-01-23 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20200910_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_friends', to=settings.AUTH_USER_MODEL, verbose_name='Друг')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_friends', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Друг',
                'verbose_name_plural': 'Друзья',
            },
        ),
    ]
