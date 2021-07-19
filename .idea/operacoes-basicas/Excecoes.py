lista = [1,10]
try:
    diretorio = 'C:/Users/RubioAlves/IdeaProjects/MeuPrimeiroProjetoPython/.idea/arquivos/teste.txt'
    arquivo = open(diretorio,'r')
    texto = arquivo.read()

    divisao = 10/2
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possível fazer uma divisão por 0')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando Arquivo')
    arquivo.close()

# except:
#     print('Erro desconhecido')