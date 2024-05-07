from django.db import models
from django import utils
from django.contrib.auth.models import User


class CustomUser(User):

    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = 'Professore'

class Turma(models.Model):
    codigoTurma = models.CharField('Codigo Turma', max_length=8)
    dataInicio = models.DateField('Data Inicio')
    descricao = models.CharField('Descricao', max_length=8)
    ano = models.CharField('Ano',max_length=2)

    def __str__(self):
        return f'{self.descricao}'

    # class Meta:
    #     verbose_name = 'Turma'


class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    sexo = models.CharField('Sexo', max_length=1)
    dataNascimento = models.DateField('Data Nascimento')
    ra = models.CharField('RA', max_length=8)
    turmaAtual = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Professor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    numeroRegistro = models.CharField('Numero registro', max_length=8)
    email = models.CharField('E-mail', max_length=100)
    senha = models.CharField('Senha', max_length=8)
    username = models.CharField('Nome Usuario', max_length=30, default="null")

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
    


class ProfessorTurma(models.Model):
    id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='turmas')
    id_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.id_professor} {self.id_turma}'
    
    class Meta:
        verbose_name = 'Relação Professor / Turma'



class Categoria(models.Model):
    categoria_nome = models.CharField('Categoria', max_length=20)

    def __str__(self):
        return f'{self.categoria_nome}'


class HistoricoMedicoes(models.Model):
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    altura = models.FloatField('Altura', max_length=100)
    peso = models.FloatField('Peso')
    imc = models.FloatField('IMC')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    timeStamp = models.DateField('TS', default=utils.timezone.now)
    id_turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Historico de Mediçõe'
