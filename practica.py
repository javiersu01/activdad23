
from bs4 import BeautifulSoup
with open('practica1.xml') as f:
    data=f.read()
#print(data)

descripcion=BeautifulSoup(data, 'xml')
#print(descripcion)

poductos=descripcion.find_all('poductos')
#print(poductos)

b_name = descripcion.find('Producto', {'ID':'100001'})
#print(b_name)

for tag in descripcion.find_all('Producto', {'ID':'100001'}):
    tag['precio'] = "9.95"
print(descripcion.prettify())