# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


#CRIANDO O JSON

import json

dicionario = {"1":1000, "2":1500, "3": 7000, "4": 756, "5":1500, "6":1500 , "7":1500, "8":1500, "9":1500, "10":1500, "11":1500, "12":1500, "13":1500, "14":1500, "15":1500,
              "16":1000, "17":1500, "18": 0, "19": 0, "20":1500, "21":1500 , "22":1500, "23":0, "24":1500, "25":1500, "26":0, "27":0, "28":1500, "29":1500,
              "30":1000}

with open("arquivo.json", "w", encoding="utf-8") as arquivo:
    arquivo = json.dump(dicionario, arquivo)

#CONTINUAÇÃO DO PROGRAMA APÓS CRIAÇÃO DO JSON

with open("arquivo.json", "r") as arquivo:
    dict_arquivo = json.load(arquivo)
    vetor_faturamento = []
    for value in dict_arquivo.values():
        vetor_faturamento.append(value)
    
    #CALCULO MENOR VALOR DE FATURAMENTO (SEM CONTAR COM FATURAMENTO NULO) - SEM UTILIZAR A FUNÇÃO PRONTA min()

    menor_valor = vetor_faturamento[0]

    for i in range(len(vetor_faturamento)):
        if (vetor_faturamento[i] != 0) and (vetor_faturamento[i] < menor_valor):
            menor_valor = vetor_faturamento[i]

    print(f"Menor valor de faturamento: {menor_valor}")
    
    #CALCULO MAIOR VALOR DE FATURAMENTO (SEM CONTAR COM FATURAMENTO NULO) - SEM UTILIZAR A FUNÇÃO PRONTA max()

    maior_valor = vetor_faturamento[0]

    for i in range(len(vetor_faturamento)):
        if (vetor_faturamento[i] != 0) and (vetor_faturamento[i] > maior_valor):
            maior_valor = vetor_faturamento[i]
    
    print(f"Maior valor de faturamento: {maior_valor}")

    #CALCULO MÉDIA FATURAMENTOS (EXCLUINDO FATURAMENTOS NULOS) - SEM UTILIZAR FUNÇÕES PRONTAS

    somatorio = 0
    nao_nulos = 0

    for i in range(len(vetor_faturamento)):
        if vetor_faturamento[i] != 0:
            somatorio += vetor_faturamento[i]
            nao_nulos += 1
    
    media_valores = somatorio / nao_nulos
    
    #CALCULO NÚMERO DE DIAS EM QUE O FATURAMENTO DIÁRIO FOI MAIOR QUE A MÉDIA MENSAL

    faturamento_diario = 0

    for valor in vetor_faturamento:
        if valor > media_valores:
            faturamento_diario += 1
    
    print(f"Número em dias em que o faturamento diário foi maior que a média mensal: {faturamento_diario}")