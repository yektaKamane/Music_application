from bs4 import BeautifulSoup
import requests
import urllib


html_text = requests.get('https://freemp3cloud.com/').text
soup = BeautifulSoup(html_text, 'lxml')
search_input = soup.find_all('input', class_ = "el-input__inner")

print(search_input)
#print((html_text).encode('utf8'))
