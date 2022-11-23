import BeatifulSoup


print('prueba en python')

with open('Clientes.xml','r') as f:
    data=f.read()
print(data)

Bs_data=BeatifulSoup(data,'xml')
print(Bs_data)