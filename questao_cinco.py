# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

string_informada = input("Digite uma palavra para invertê-la: ")

lista_informada = list(string_informada)

lista_invertida = []

for i in range((len(lista_informada) - 1), -1, -1):
   lista_invertida.append(lista_informada[i])

string_invertida = ''.join(lista_invertida)

print(string_invertida)