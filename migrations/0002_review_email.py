# Generated by Django 2.2.5 on 2021-10-01 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InlineSpeedSkates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.EmailField(default='', max_length=255, verbose_name='email address'),
        ),
    ]