from django.contrib import admin
from .models import *

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Categoria)
admin.site.register(Turma)
admin.site.register(HistoricoMedicoes)
admin.site.register(ProfessorTurma)