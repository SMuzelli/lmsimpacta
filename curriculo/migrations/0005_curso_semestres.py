# Generated by Django 2.1.7 on 2019-05-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0004_auto_20190521_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='semestres',
            field=models.IntegerField(default=4),
        ),
    ]
