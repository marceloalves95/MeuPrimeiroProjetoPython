lista_animal = ['cachorro','gato','elefante', 'lobo','arara']
print(lista_animal)
#A Tupla é como se fosse uma lista imutável em Kotlin, por exemplo.
#Não é possível alterá-la depois da sua criação.
tupla = (1,10,12,14)
#Comando inválido -> tupla[0] = 12

#É possível converter um vetor em uma tupla, usando o comando tuple.
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

#Também é possível converter uma tupla em um vetor/lista. Usando o comando list.
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)
