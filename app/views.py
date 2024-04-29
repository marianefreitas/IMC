from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import HistoricoMedicoes, Categoria, Aluno, Turma
from django.db.models import Count, Q
from django.http import JsonResponse


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.warning(request, ('Usuário não encontrado!'))
            return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    # messages.success(request, ("Você foi deslogado com sucesso"))
    return redirect('home')


def home(request):
    return render(request, 'index.html', {})


def dashboard(request):
    if request.user.is_authenticated:
        historico = HistoricoMedicoes.objects.all()
        total = historico.count()
        imc_outlier = HistoricoMedicoes.objects.select_related("categoria").filter(~Q(categoria = 2)).count()
        imc_padrao = HistoricoMedicoes.objects.select_related("categoria").filter(categoria =2).count()

        print(imc_outlier)
        print(imc_padrao)
        return render(request, 'dashboard.html', {'historico':historico,'total':total,'imc_padrao':imc_padrao,'imc_outlier':imc_outlier})
    else:
        messages.warning(request, ('Faça seu login!'))
        return render(request, 'dashboard.html', {})
    

def graficoImcGeral(request):
    if request.user.is_authenticated:
        primeiro = HistoricoMedicoes.objects.select_related("categoria","id_aluno","id_aluno__turmaAtual").filter(id_aluno__turmaAtual__codigoTurma__startswith='1').annotate(dcount=Count('categoria__categoria_nome')).order_by('categoria__categoria_nome')
        
        #.values('id_aluno__turmaAtual__descricao')
        # primeiro = primeiro.select_related("turmaAtual").all()
        # for p in HistoricoMedicoes.objects.raw("""SELECT COUNT(categoria_nome) FROM app_historicomedicoes 
        #                                        INNER JOIN app_categoria  ON app_categoria.id = app_historicomedicoes.categoria_id
        #                                        INNER JOIN app_aluno  ON app_aluno.id = app_historicomedicoes.id_aluno_id
        #                                        INNER JOIN app_turma  ON app_turma.id =app_aluno.turmaAtual_id
        #                                        WHERE app_turma.codigoTurma LIKE '1%'
        #                                        GROUP BY app_categoria.categoria_nome
        #                                        ORDER BY app_categoria.id"""):
        #     print(p)
        print(primeiro)
        data_json = {'teste':list(primeiro.values())}  
        return JsonResponse(data_json)
    else:
            messages.warning(request, ('Usuário não encontrado!'))
            return render(request, 'login.html', {})
