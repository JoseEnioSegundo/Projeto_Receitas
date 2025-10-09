from django.test import Client
import re
c=Client()
r=c.get('/')
print('status', r.status_code)
s=r.content.decode()
m=re.search(r'<img[^>]+src=["\']([^"\']+)["\']', s)
print('first img src ->', m.group(1) if m else 'no img')
