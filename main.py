import requests

API_KEY = "e81448fc9d257aa51168b38432572933"
cidade = "rio de janeiro"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}"

requisicao = requests.get(link)
print(requisicao.json())