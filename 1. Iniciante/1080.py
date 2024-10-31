lista = []

for i in range(100):
    lista.append(int(input()))
    
print(max(lista))
print(lista.index(max(lista))+1)