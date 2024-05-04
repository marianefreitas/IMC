from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError, DatabaseError
from .models import Professor, Turma, Aluno, HistoricoMedicoes, Categoria
from .service import calcular_imc_percentil


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("turmas")
        else:
            messages.warning(request, ('Usuário não encontrado!'))
            return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request, 'index.html', {})


def dashboard(request):
    if request.user.is_authenticated:

        return render(request, 'dashboard.html', {})
    else:
        messages.warning(request, ('Faça seu login!'))
        return render(request, 'login.html', {})


def turmas(request):
    if request.user.is_authenticated:

        professor = Professor.objects.get(username=request.user.username)
        turmas = professor.turmas.all()

        context = {
            "turmas": turmas,
            "turma_selecionada": None,
            "alunos": None
        }

        turma_id = request.session.get('turma_id')

        if request.method == 'POST':
            turma_id = request.POST.get('turma')
            request.session['turma_id'] = turma_id

        if turma_id:
            turma_selecionada = Turma.objects.get(id=turma_id)
            alunos = Aluno.objects.filter(turmaAtual=turma_selecionada).order_by('nome')

            context.update({
                "turma_selecionada": turma_selecionada,
                "alunos": alunos
            })

        return render(request, 'turmas.html', context)

    else:
        return render(request, 'login.html', {})


def adicionar_medidas(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            aluno_id = request.POST.get('aluno_id')
            altura = float(request.POST.get('altura', 0))
            peso = float(request.POST.get('peso', 0))

            # Validações básicas - Não estou conseguindo fazer as mensagens aparecerem
            # if not (1.0 <= altura <= 2.5):
            #     print('Entrei no IF da validação')

            #     messages.error(request, ('Altura fora do intervalo permitido.'))
            #     return redirect("adicionar_medidas")

            # if not (10 <= peso <= 200):
            #     messages.error(request, 'Peso fora do intervalo permitido.')
            #     return redirect("adicionar_medidas")
            try:
                aluno = Aluno.objects.get(id=aluno_id)

                imc, categoria = calcular_imc_percentil(aluno, peso, altura)

                nova_medicao = HistoricoMedicoes(
                    id_aluno=aluno,
                    altura=altura,
                    peso=peso,
                    imc=imc,
                    categoria=Categoria.objects.get(id=categoria)
                )

                nova_medicao.save()
                messages.success(request, 'Medidas adicionadas com sucesso!')
            except (Aluno.DoesNotExist, Categoria.DoesNotExist):
                messages.error(request, 'Aluno ou categoria não encontrado.')
            except (IntegrityError, DatabaseError):
                messages.error(request, 'Erro ao salvar no banco de dados.')
            except Exception as e:
                messages.error(request, f'Erro ao adicionar medidas: {str(e)}')

        return redirect("turmas")
    else:
        return render(request, 'login.html', {})
