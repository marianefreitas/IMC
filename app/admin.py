from django.contrib import admin
from .models import Aluno, Professor, Categoria, Turma, HistoricoMedicoes, ProfessorTurma




class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'senha')



admin.site.register(Aluno)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Categoria)
admin.site.register(Turma)
admin.site.register(HistoricoMedicoes)
admin.site.register(ProfessorTurma)
