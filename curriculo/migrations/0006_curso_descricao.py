# Generated by Django 2.1.7 on 2019-05-21 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0005_curso_semestres'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='descricao',
            field=models.TextField(blank=True),
        ),
    ]
