conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
print('Conjunto 1: {}'.format(conjunto))
print('Conjunto 2: {}'.format(conjunto2))
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))
conjunto_diff_simetrico = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrico))
print('--------------------------------------------')
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
print('Conjunto A: {}'.format(conjunto_a))
print('Conjunto B: {}'.format(conjunto_b))
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('O conjunto a é um subconjunto de b? Resposta: {}'.format(conjunto_subset))
conjunto_subset2 = conjunto_b.issubset(conjunto_a)
print('O conjunto b é um subconjunto de a? Resposta: {}'.format(conjunto_subset2))
conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('O conjunto a é um superconjunto de b? Resposta: {}'.format(conjunto_superset))
conjunto_superset2 = conjunto_b.issuperset(conjunto_a)
print('O conjunto b é um subconjunto de a? Resposta: {}'.format(conjunto_superset2))
print('--------------------------------------------')
lista = ['cachorro','cachorro','gato','gato','elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

# conjunto = {1,2,3,4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)