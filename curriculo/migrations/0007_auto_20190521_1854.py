# Generated by Django 2.1.7 on 2019-05-21 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0006_curso_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='descricao',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
