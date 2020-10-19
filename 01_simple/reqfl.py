
import requests

r = requests.get('http://0.0.0.0:5802/') 

s = r.content

print(s)
