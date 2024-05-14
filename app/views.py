from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Professor, Turma, Aluno, HistoricoMedicoes, Categoria, ProfessorTurma
from .service import calcular_imc_percentil
from django.db import IntegrityError, DatabaseError
from .forms import FiltroForm
from django.db.models import Count, Q,  F, Value, Func
from django.db.models.functions import Concat
from django.http import JsonResponse
##########################################################################

##########################################################################


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
        filtro = FiltroForm()

        historico = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("timeStamp","altura","peso","imc","categoria__categoria_nome","id_turma__descricao").annotate(
            fullName = Concat('id_aluno__nome', Value(' '),'id_aluno__sobrenome')).order_by("-timeStamp","-id")
        total = HistoricoMedicoes.objects.all().count()
        imc_outlier = HistoricoMedicoes.objects.select_related("categoria").filter(~Q(categoria = 2)).count()
        imc_padrao = HistoricoMedicoes.objects.select_related("categoria").filter(categoria =2).count()
        data_donnut = [imc_padrao,imc_outlier]

        ##################################################
        #                  CONFIG FILTRO                #
        
        choices_nome = [(i['id_aluno'], i['id_aluno__nome'].title() + ' ' + i['id_aluno__sobrenome'].title()) for i in HistoricoMedicoes.objects.select_related("id_aluno").values("id_aluno","id_aluno__nome","id_aluno__sobrenome").distinct().order_by("id_aluno__nome")]
                        
        choices_nome.insert(0,(0,"Todos"))
        filtro.fields['nome'].choices = choices_nome

        
        choices_categoria = [(i.id, i.__str__) for i in Categoria.objects.all()]
        choices_categoria.insert(0,(0,"Todas"))
        filtro.fields['categoria'].choices = choices_categoria



        choices_turma = [(i.id, i.__str__) for i in Turma.objects.all()]
        choices_turma.insert(0,(0,"Todas"))
        filtro.fields['turma'].choices = choices_turma


        
        ##################################################

        ##################################################
        #                  GRAFICO GERAL                 #
        abaixo_peso = HistoricoMedicoes.objects.select_related("categoria","id_turma").values("id_turma__ano","categoria_id").filter(categoria_id__id = '1').annotate(dcount = Count('categoria_id')).order_by()
        peso_normal = HistoricoMedicoes.objects.select_related("categoria","id_turma").values("id_turma__ano","categoria_id").filter(categoria_id__id = '2').annotate(dcount = Count('categoria_id')).order_by()
        sobrepeso = HistoricoMedicoes.objects.select_related("categoria","id_turma").values("id_turma__ano","categoria_id").filter(categoria_id__id = '3').annotate(dcount = Count('categoria_id')).order_by()
        obesidade = HistoricoMedicoes.objects.select_related("categoria","id_turma").values("id_turma__ano","categoria_id").filter(categoria_id__id = '4').annotate(dcount = Count('categoria_id')).order_by()
        
        
        abaixo_peso = [x["dcount"] for x in abaixo_peso]
        peso_normal = [x["dcount"] for x in peso_normal]
        sobrepeso = [x["dcount"] for x in sobrepeso]
        obesidade = [x["dcount"] for x in obesidade]

        total_ab = sum(abaixo_peso)
        total_pn = sum(peso_normal)
        total_sp = sum(sobrepeso)
        total_obs = sum(obesidade)
    
        
        data_json = {'abaixo_peso':list(abaixo_peso),
                     'peso_normal':list(peso_normal),
                     'sobrepeso':list(sobrepeso),
                     'obesidade':list(obesidade)
                     
                     } 

        ##################################################



        ##################################################
        #                  GRAFICO FEMININO                #

        abaixo_peso_f = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("id_turma__ano","categoria_id").filter(categoria_id__id = '1',id_aluno_id__sexo='F').annotate(dcount = Count('categoria_id')).order_by()
        peso_normal_f = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("id_turma__ano","categoria_id").filter(categoria_id__id = '2',id_aluno_id__sexo='F').annotate(dcount = Count('categoria_id')).order_by()
        sobrepeso_f = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("id_turma__ano","categoria_id").filter(categoria_id__id = '3',id_aluno_id__sexo='F').annotate(dcount = Count('categoria_id')).order_by()
        obesidade_f = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("id_turma__ano","categoria_id").filter(categoria_id__id = '4',id_aluno_id__sexo='F').annotate(dcount = Count('categoria_id')).order_by()
        
        
        abaixo_peso_f = [x["dcount"] for x in abaixo_peso_f]
        peso_normal_f = [x["dcount"] for x in peso_normal_f]
        sobrepeso_f = [x["dcount"] for x in sobrepeso_f]
        obesidade_f = [x["dcount"] for x in obesidade_f]
        
        data_json_f = {'abaixo_peso':list(abaixo_peso_f),
                     'peso_normal':list(peso_normal_f),
                     'sobrepeso':list(sobrepeso_f),
                     'obesidade':list(obesidade_f)
                     
                     } 
        ##################################################


        ##################################################
        #                  GRAFICO MASCULINO             #

        abaixo_peso_m = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("id_turma__ano","categoria_id").filter(categoria_id__id = '1',id_aluno_id__sexo='M').annotate(dcount = Count('categoria_id')).order_by()
        peso_normal_m = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("id_turma__ano","categoria_id").filter(categoria_id__id = '2',id_aluno_id__sexo='M').annotate(dcount = Count('categoria_id')).order_by()
        sobrepeso_m = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("id_turma__ano","categoria_id").filter(categoria_id__id = '3',id_aluno_id__sexo='M').annotate(dcount = Count('categoria_id')).order_by()
        obesidade_m = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("id_turma__ano","categoria_id").filter(categoria_id__id = '4',id_aluno_id__sexo='M').annotate(dcount = Count('categoria_id')).order_by()
        
        
        abaixo_peso_m = [x["dcount"] for x in abaixo_peso_m]
        peso_normal_m = [x["dcount"] for x in peso_normal_m]
        sobrepeso_m = [x["dcount"] for x in sobrepeso_m]
        obesidade_m = [x["dcount"] for x in obesidade_m]
        
        data_json_m = {'abaixo_peso':list(abaixo_peso_m),
                     'peso_normal':list(peso_normal_m),
                     'sobrepeso':list(sobrepeso_m),
                     'obesidade':list(obesidade_m)
                     
                     } 
        

        if request.method == "POST":
            
            
            temp_nome = request.POST['nome']
            temp_categoria = request.POST['categoria']
            temp_turma = request.POST['turma']
            temp_order = request.POST['order']

            filtro.fields['nome'].initial = temp_nome
            filtro.fields['categoria'].initial = temp_categoria
            filtro.fields['turma'].initial = temp_turma
            filtro.fields['order'].initial = temp_order


            # FILTRA NOME , CATEGORIA E TURMA

            if temp_nome == "0" and temp_categoria == "0" and temp_turma == "0":
                historico = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("timeStamp","altura","peso","imc","categoria__categoria_nome","id_turma__descricao").annotate(
                            fullName = Concat('id_aluno__nome', Value(' '),'id_aluno__sobrenome'))
                
            elif temp_nome != "0" and temp_categoria == "0" and temp_turma == "0":
                historico = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("timeStamp","altura","peso","imc","categoria__categoria_nome","id_turma__descricao").filter(id_aluno = temp_nome).annotate(
                            fullName = Concat('id_aluno__nome', Value(' '),'id_aluno__sobrenome'))
    
            elif temp_nome != "0" and temp_categoria != "0" and temp_turma == "0":
                historico = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("timeStamp","altura","peso","imc","categoria__categoria_nome","id_turma__descricao").filter(id_aluno = temp_nome,categoria = temp_categoria).annotate(
                            fullName = Concat('id_aluno__nome', Value(' '),'id_aluno__sobrenome'))
            
            elif temp_nome != "0" and temp_categoria != "0" and temp_turma != "0":
                historico = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("timeStamp","altura","peso","imc","categoria__categoria_nome","id_turma__descricao").filter(id_aluno = temp_nome,categoria = temp_categoria, id_turma = temp_turma).annotate(
                            fullName = Concat('id_aluno__nome', Value(' '),'id_aluno__sobrenome'))
            
            elif temp_nome == "0" and temp_categoria != "0" and temp_turma == "0":
                historico = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("timeStamp","altura","peso","imc","categoria__categoria_nome","id_turma__descricao").filter(categoria = temp_categoria).annotate(
                            fullName = Concat('id_aluno__nome', Value(' '),'id_aluno__sobrenome'))
            
            elif temp_nome == "0" and temp_categoria == "0" and temp_turma != "0":
                historico = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("timeStamp","altura","peso","imc","categoria__categoria_nome","id_turma__descricao").filter(id_turma = temp_turma).annotate(
                            fullName = Concat('id_aluno__nome', Value(' '),'id_aluno__sobrenome'))
            
            elif temp_nome == "0" and temp_categoria != "0" and temp_turma != "0":
                historico = HistoricoMedicoes.objects.select_related("categoria","id_turma","id_aluno").values("timeStamp","altura","peso","imc","categoria__categoria_nome","id_turma__descricao").filter(categoria = temp_categoria,id_turma = temp_turma).annotate(
                            fullName = Concat('id_aluno__nome', Value(' '),'id_aluno__sobrenome'))
                
            # ORDENA OS OBJETOS
            if temp_order == '0':
                historico = historico.order_by("-timeStamp","-id")
            elif temp_order == '1':
                historico = historico.order_by("timeStamp",'id')
            elif temp_order == '2':
                historico = historico.order_by("fullName")
            elif temp_order == '3':
                historico = historico.order_by("-fullName")


            

    



        
        return render(request, 'dashboard.html', {'historico':historico,'total':total,'imc_padrao':imc_padrao,
                                                  'imc_outlier':imc_outlier,'data_json':data_json,'data_json_f':data_json_f,
                                                  'data_json_m':data_json_m,'data_donnut':data_donnut,'filtro':filtro,
                                                  'total_ab':total_ab,'total_pn':total_pn,'total_sp':total_sp,'total_obs':total_obs})
    else:
        messages.warning(request, ('Faça seu login!'))
        return redirect('login')
        


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
            turma_id = request.POST.get('turma_id')

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
                    id_turma = Turma.objects.get(id= turma_id),
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
        messages.warning(request, ('Faça seu login!'))
        return redirect('login')
    


    

