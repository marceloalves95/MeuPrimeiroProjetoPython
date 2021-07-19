a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

soma = a + b
subtracao = a-b
multiplicacao = a*b
divisao = a/b
resto = a%b

print('')

#Essa linha informa qual é o tipo da váriavel
#print(type(soma))
#Nessa linha você converte a várivel soma para String
#soma = str(soma)
#Aqui você concatena várivel de soma
print('Soma: ' + str(soma))
#Essa linha formata a váriavel como o exemplo acima
#print('Soma: {}'.format(soma))
print('Subtração: ' + str(subtracao))
print('Multiplicação: ' + str(multiplicacao))
print('Divisão: ' + str(divisao))
print('Resto: ' + str(resto))