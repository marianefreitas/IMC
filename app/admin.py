from django.contrib import admin
from .models import Aluno, Professor, Categoria, Turma, HistoricoMedicoes, ProfessorTurma


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'senha')


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'turmaAtual')


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('codigoTurma', 'descricao')


class ProfessorTurmaAdmin(admin.ModelAdmin):
    list_display = ('id_professor', 'id_turma')


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Categoria)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(HistoricoMedicoes)
admin.site.register(ProfessorTurma, ProfessorTurmaAdmin)
