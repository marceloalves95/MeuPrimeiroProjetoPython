contador_letras = lambda lista:[len(x) for x in lista]

lista_animais = ['cachorro','gato','elefante']
print(contador_letras(lista_animais))

soma = lambda a,b:a + b
subtracao = lambda a,b:a - b
multiplicacao = lambda a,b:a * b
divisao = lambda a,b:a / b

print('A soma : {}'.format(soma(5,10)))
print('A subtração : {}'.format(subtracao(5,10)))
print('A multiplicação : {} '.format(multiplicacao(5,10)))
print('A divisão : {}'.format(divisao(5,10)))

calculadora = {
    'soma':lambda a, b:a + b,
    'subtracao':lambda a, b:a - b,
    'multiplicao':lambda a, b:a * b,
    'divisao':lambda a, b:a / b
}

print(type(calculadora))
soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicao = calculadora['multiplicao']
divisao = calculadora['divisao']

print('A soma : {}'.format(soma(10,5)))
print('A subtração : {}'.format(subtracao(10,5)))
print('A multiplicação : {} '.format(multiplicacao(10,2)))
print('A divisão : {}'.format(divisao(10,5)))
