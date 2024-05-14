import requests

API_KEY = "e81448fc9d257aa51168b38432572933"
cidade = "fortaleza"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}"

try:
    # Realiza a requisição
    requisicao = requests.get(link)

    # Verifica se a requisição foi bem-sucedida
    if requisicao.status_code == 200:
        # Converte a resposta para JSON
        dados = requisicao.json()

        # Extrai os campos específicos da resposta
        temperatura = dados['main']['temp']
        nova_temperatura = temperatura - 273,15
        descricao_do_clima = dados['weather'][0]['description']
        localizacao = dados['name']

        # Imprime os dados de forma organizada
        print(f"Temperatura em K: {temperatura}K")
        print(f"Temperatura em C: {nova_temperatura}c")
        print(f"Descrição do Clima: {descricao_do_clima}")
        print(f"Cidade: {localizacao}")
    else:
        print("Erro ao buscar dados do clima.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
