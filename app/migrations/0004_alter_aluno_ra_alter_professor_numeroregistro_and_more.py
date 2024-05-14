# Generated by Django 5.0.3 on 2024-05-13 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_turma_datainicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='ra',
            field=models.CharField(max_length=100, verbose_name='RA'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='numeroRegistro',
            field=models.CharField(max_length=100, verbose_name='Numero registro'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='senha',
            field=models.CharField(max_length=100, verbose_name='Senha'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='codigoTurma',
            field=models.CharField(max_length=30, verbose_name='Codigo Turma'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='descricao',
            field=models.CharField(max_length=100, verbose_name='Descricao'),
        ),
    ]
