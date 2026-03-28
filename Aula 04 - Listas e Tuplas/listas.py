lista = [10, 20, 30, 40, 50]
print(lista[1])
print(lista[1:3])
print(20 in lista)
print(60 in lista)
print(lista.pop(1))
print(lista)

tupla = (10, 20, 30, 40, 50)
print(tupla[1])
print(tupla[1:3])
print(20 in tupla)
print(60 in tupla)

tupla1 = (1, 2)
tupla2 = (3, 4)
nova_tupla = tupla1 + tupla2
print(nova_tupla)

lista1 = [1, 2, 3, 4]
for i in lista:
    print(i)

tupla3 = (1, 2, 3, 4)
for i in tupla3:
    print(i)

tupla4 = (1, 2, 3)
a, b, c = tupla4
print(a, b, c)

lista2 = [1, 2, 3]
x, y, z = lista2
print(x, y, z)

tarefas = ["Estudar Python", "Fazer compras", "Lavar a louça"]
tarefas.append("Ler um livro")
tarefas.remove("Fazer compras")
for i in tarefas:
    print(i)

cidade1 = ("São Paulo", -23.5505, -46.6333)
cidade2 = ("Rio de Janeiro", -22.9068, -43.1729)
cidade3 = ("Brasília", -15.7801, -47.9292)

cidades = [cidade1, cidade2, cidade3]

for cidade in cidades:
    nome, latidude, longitude = cidade
    print(f"Cidade: {nome}, Latitude: {latidude}, Longitude: {longitude}")