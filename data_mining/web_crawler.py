import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):
    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')
    for each_text in soup.find_all('div', {'class': 'entry-content'}):
        content = each_text
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%¨&*()_+-=´[]~;/`{^}:?.,\|'
    return

