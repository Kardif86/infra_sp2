# Generated by Django 2.2.16 on 2022-11-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_auto_20221101_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True,
                                    verbose_name='Почта'),
        ),
    ]
