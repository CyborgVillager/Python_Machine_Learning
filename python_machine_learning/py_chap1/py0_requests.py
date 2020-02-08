from py_chap1_source import *

request = requests.get(r'https://api.github.com/users/CyborgVillager/starred')
print(request.json())
