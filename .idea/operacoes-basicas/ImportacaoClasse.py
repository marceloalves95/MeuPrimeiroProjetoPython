#Cada arquivo do Python é um módulo
from Televisao import Televisao
from ContadorLetras import contador_letras

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

if __name__ == '__main__':
    lista = ['cachorro','gato','elefante']
    total_letras = contador_letras(lista)
    print('O total de letras por palavra da lista é: {}'.format(total_letras))