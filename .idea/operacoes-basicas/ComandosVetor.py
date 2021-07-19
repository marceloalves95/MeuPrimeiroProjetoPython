lista = [12,10,7,5]
lista_animal = ['cachorro','gato','elefante', 'lobo','arara']

#O comando append acrescenta um valor a um vetor.
lista_animal.append('leão')
print(lista_animal)
#O comando pop remove o último item de um vetor. Ou uma posição especifica
lista_animal.pop(1)
print(lista_animal)
#O comando remove tem a mesma função do pop. Ele remove um item de um vetor.
lista_animal.remove('elefante')
print(lista_animal)
#O comando sort ordena uma lista em ordem alfabeta e crescente.
lista.sort()
print(lista)
#O comando reverse ordena uma lista em ordem alfabeta e decrescente. Ele é oposto ao comando sort().
lista.reverse()
print(lista)
#O comando len conta quantos elementos têm em um vetor.
print(len(lista_animal))
#O comando sum soma todos os valores de um vetor.
print(sum(lista))
#Retorna o maior valor de um vetor.
print(max(lista))
#Retorna o menor valor da um vetor.
print(min(lista))


#print(lista_animal[1])
# nova_lista = lista_animal * 3
# print(nova_lista)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista')
# else:
#     print('Não existe um lobo na lista. Será incluído')


