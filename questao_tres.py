# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

#CONSUMINDO JSON

import json

with open("dados.json", "r") as arquivo:
    vetor_inicial = json.load(arquivo)
    vetor_faturamento = []
    for dicts in vetor_inicial:
        vetor_faturamento.append(dicts["valor"])
    
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
