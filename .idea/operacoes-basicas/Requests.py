import requests

def retorna_dados_cep(cep):

    base_url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
    response = requests.get(base_url)
    print(response.status_code)
    print(response.text)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    return dados_cep

if __name__ == '__main__':
    retorna_dados_cep('01001000')