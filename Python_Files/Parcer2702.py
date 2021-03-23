import requests
from bs4 import BeautifulSoup


url = 'https://minfin.com.ua/currency/nbu/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('table', {'class':'table-auto'})
tr = table.find_all('td', {'class': 'responsive-hide'})

print(tr)