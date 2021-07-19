# nota = int(input('Entre com a sua nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida.Entre com a nota correta: '))
# print(nota)

a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Quarto Bimestre: '))
media = (a + b + c + d)/4
print('Média aritmetica: {}'.format(media))