import requests

API_KEY = ""
cidade = "rio de janeiro"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}"

requisicao = requests.get(link)
print(requisicao.json())