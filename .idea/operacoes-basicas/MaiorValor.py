a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

if a > b and a > c:
    print('O maior valor é: {}'.format(a))
elif b> a and b > c:
    print('O maior valor é: {}'.format(b))
else:
    print('O maior valor é: {}'.format(c))
#O comando abaixo está fora do if por causa da indentação
print('Fim do programa')