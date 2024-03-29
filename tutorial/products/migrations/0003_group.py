# Generated by Django 5.0.2 on 2024-03-01 08:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_lesson_options_alter_product_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название группы')),
                ('min_users', models.PositiveIntegerField(verbose_name='Минимальное количество участников')),
                ('max_users', models.PositiveIntegerField(verbose_name='Максимальное количество участников')),
                ('members', models.ManyToManyField(related_name='product_groups', to=settings.AUTH_USER_MODEL, verbose_name='Ученики, состоящие в группе')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'группы',
                'verbose_name_plural': 'группы',
            },
        ),
    ]
