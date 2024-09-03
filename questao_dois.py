# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
# pertence ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

vetor_inicial = [0, 1]

indice = 0

encerrar = False

try:
    numero_informado = int(input("Digite o número para verificar se ele está na sequência Fibonacci: "))
    while not encerrar:
        numero_gerado = vetor_inicial[indice] + vetor_inicial[indice + 1]
        vetor_inicial.append(numero_gerado)
        indice += 1
        if numero_gerado == numero_informado:
            resultado = "O número informado pertence à sequência de Fibonacci"
            encerrar = True
        elif numero_gerado > numero_informado:
            resultado = "O número informado não pertence à sequência de Fibonacci"
            encerrar = True
    print(resultado)
except ValueError:
    print("Número digitado inválido!")