from bs4 import BeautifulSoup
import requests

site_data = requests.get('https://www.climatempo.com.br/').content

soup = BeautifulSoup(site_data, 'html.parser')

#print(soup.prettify())
#print(soup.get_text('<title>'))
print(soup.get_text('Temperatura máxima'))