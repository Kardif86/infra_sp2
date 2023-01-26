# Generated by Django 2.2.16 on 2022-11-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0006_auto_20221102_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(
                choices=[('user', 'User'), ('moderator', 'Moderator'),
                         ('admin', 'Admin')], default='user', max_length=20),
        ),
    ]