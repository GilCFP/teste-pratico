import requests
import json

url = "http://127.0.0.1:5000/api/search"

payload = {
    'day': '6s',
    'month': '03',
    'year': '2024',
    'quantity': {'little': 10, 'big': 5},
    'password': '123456789'
}

# Serializa os dados do payload em formato JSON
payload_json = json.dumps(payload)

# Define o cabeçalho Content-Type como application/json
headers = {'Content-Type': 'application/json'}

# Faz a solicitação POST com os dados JSON e cabeçalhos apropriados
response = requests.post(url, headers=headers, data=payload_json)

print(response.json())