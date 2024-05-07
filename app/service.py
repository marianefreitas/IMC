from datetime import date
from .models import Categoria
from datetime import datetime

PERCENTIS_IMC = {
    'M': {
        '6': 14.54,
        '7': 15.07,
        '8': 15.62,
        '9': 16.17,
        '10': 16.72,
        '11': 17.28,
        '12': 17.87,
        '13': 18.53,
        '14': 19.22,
        '15': 19.92,
        '16': 20.63,
        '17': 21.12,
        '18': 21.45,
        '19': 21.86,
        '20': 23.07,
        '21': 23.07,
        '22': 23.07,
        '23': 23.07,
        '24': 23.07,
        '25': 24.19,
        '26': 24.19,
        '27': 24.19,
        '28': 24.19,
        '29': 24.19,
        '30': 24.90,
        '31': 24.90,
        '32': 24.90,
        '33': 24.90,
        '34': 24.90,
        '35': 25.25,
        '36': 25.25,
        '37': 25.25,
        '38': 25.25,
        '39': 25.25,
        '40': 25.49,
        '41': 25.49,
        '42': 25.49,
        '43': 25.49,
        '44': 25.49,
        '45': 25.55,
        '46': 25.55,
        '47': 25.55,
        '48': 25.55,
        '49': 25.55,
        '50': 25.54,
        '51': 25.54,
        '52': 25.54,
        '53': 25.54,
        '54': 25.54,
        '55': 25.51,
        '56': 25.51,
        '57': 25.51,
        '58': 25.51,
        '59': 25.51,
        '60': 25.47,
        '61': 25.47,
        '62': 25.47,
        '63': 25.47,
        '64': 25.47,
        '65': 25.41,
        '66': 25.41,
        '67': 25.41,
        '68': 25.41,
        '69': 25.41,
        '70': 25.33,
        '71': 25.33,
        '72': 25.33,
        '73': 25.33,
        '74': 25.33,
    },
    'F': {
        '6': 14.31,
        '7': 14.98,
        '8': 15.66,
        '9': 16.33,
        '10': 17.00,
        '11': 17.67,
        '12': 18.35,
        '13': 18.95,
        '14': 19.32,
        '15': 19.69,
        '16': 20.09,
        '17': 20.36,
        '18': 20.57,
        '19': 20.80,
        '20': 21.45,
        '21': 21.45,
        '22': 21.45,
        '23': 21.45,
        '24': 21.45,
        '25': 22.10,
        '26': 22.10,
        '27': 22.10,
        '28': 22.10,
        '29': 22.10,
        '30': 22.69,
        '31': 22.69,
        '32': 22.69,
        '33': 22.69,
        '34': 22.69,
        '35': 23.25,
        '36': 23.25,
        '37': 23.25,
        '38': 23.25,
        '39': 23.25,
        '40': 23.74,
        '41': 23.74,
        '42': 23.74,
        '43': 23.74,
        '44': 23.74,
        '45': 24.17,
        '46': 24.17,
        '47': 24.17,
        '48': 24.17,
        '49': 24.17,
        '50': 24.54,
        '51': 24.54,
        '52': 24.54,
        '53': 24.54,
        '54': 24.54,
        '55': 24.92,
        '56': 24.92,
        '57': 24.92,
        '58': 24.92,
        '59': 24.92,
        '60': 25.29,
        '61': 25.29,
        '62': 25.29,
        '63': 25.29,
        '64': 25.29,
        '65': 25.66,
        '66': 25.66,
        '67': 25.66,
        '68': 25.66,
        '69': 25.66,
        '70': 26.01,
        '71': 26.01,
        '72': 26.01,
        '73': 26.01,
        '74': 26.01,
    }
}


def calcular_imc_percentil(aluno, peso, altura):
    # if aluno.dataNascimento is datetime:
    idade = date.today().year - aluno.dataNascimento.year
    # else:
    #     dataNsc = datetime.strptime(aluno.dataNascimento, '%d/%m/%y %H:%M:%S')
    #     idade = date.today().year - dataNsc
        
    # print(f' idade  ==> {aluno.dataNascimento.year}')
    # print(f' idade calculada ==> {idade}')
    sexo = aluno.sexo
    # print(f'sexo aluno ===> {aluno.sexo}')
    imc = peso / (altura ** 2)
    # print(f' IMC ===> {imc}')
    imc_perc_50 = PERCENTIS_IMC[sexo][str(idade)]

    # Calcule a % de adequação do IMC
    adequacao = (imc / imc_perc_50) * 100

    # Determine a categoria
    if adequacao > 160:
        categoria_nome = "Obesidade"
    elif adequacao > 139.99:
        categoria_nome = "Obesidade"
    elif adequacao > 129.99:
        categoria_nome = "Obesidade"
    elif adequacao > 110.99:
        categoria_nome = "Sobrepeso"
    elif adequacao < 79.99:
        categoria_nome = "Abaixo do peso"
    else:
        categoria_nome = "Peso Normal"

    categoria = Categoria.objects.get(categoria_nome=categoria_nome)

    return imc, categoria.id
