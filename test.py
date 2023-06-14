import requests
from bs4 import BeautifulSoup

# url = 'https://www.naver.com'
url = 'https://weather.naver.com/'
res = requests.get(url)
# print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
a = soup.find(class_ = 'today_weather')
print(a)