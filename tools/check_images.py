from django.test import Client
from bs4 import BeautifulSoup

c = Client()
resp = c.get('/')
print('status', resp.status_code)
html = resp.content.decode()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find('img')
print('first img src ->', img['src'] if img else 'no img')
