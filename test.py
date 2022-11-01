import requests
import random

url = "https://pastebin.com/raw/"
r = requests.get(url+"eMaHmi3F").text.split(';')
print(random.choice(r).strip())
