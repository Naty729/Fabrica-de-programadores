
import bs4 # Importa a biblioteca Beautifulsoup 4
import requests # Importara biblioteca requests 

url = "https://quotes.toscrape.com/" # Grava o site quotes 
quotes = requests.get(url) # Importa o código do site 
soup = bs4.BeautifulSoup(quotes.text , 'html.parser') # Converte o quote em html

frase = soup.find_all('div', class_='quote')

for div in frase:
    texto = div.find('span', class_='text')