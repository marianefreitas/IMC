# Generated by Django 5.0.3 on 2024-05-13 23:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_aluno_ra_alter_professor_numeroregistro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicomedicoes',
            name='timeStamp',
            field=models.DateField(default=datetime.date(2024, 5, 13), verbose_name='TS'),
        ),
    ]