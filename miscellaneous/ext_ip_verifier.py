import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

response = urlopen(url)

data = json.load(response)
ip = data['ip']
org = data['org']
city = data['city']
region = data['region']
country = data['country']

print('Detalhes do seu IP externo\n')
print(f' IP: {ip}\n Provedor: {org}\n Cidade: {city}\n Estado: {region}\n País: {country} ')
