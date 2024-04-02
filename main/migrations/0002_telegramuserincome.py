# Generated by Django 5.0.3 on 2024-03-31 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUserIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='От куда пришёл доход.', max_length=100, verbose_name='Название дохода')),
                ('amount', models.BigIntegerField(help_text='Сумма дохода.', verbose_name='Сумма')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Временная метка, указывающая, когда был создан доход.', verbose_name='Создан')),
                ('user', models.ForeignKey(help_text='Пользователь Telegram, которому принадлежит доход.', on_delete=django.db.models.deletion.CASCADE, to='main.telegramuser', verbose_name='Пользователь Telegram')),
            ],
            options={
                'verbose_name': 'Доход Telegram',
                'verbose_name_plural': 'Доходы Telegram',
                'ordering': ['-created_at'],
            },
        ),
    ]