bike=["lala","lala2","lala3"]
print(bike)
print(bike[1])

# Insercao no indice desejado
bike.insert(4,"a")
print(bike)
bike.insert(5,"c")
print(bike)
bike.insert(6,"b")
print(bike)

# Insercao no fim da lista
bike.append("ajkdhaiudqwiehjkzchiuzxuciadqiwe")
print(bike)
bike.sort()
print(bike)

# Remocao do elemento desejado
bike.remove("lala2")
print(bike)

# Remove o elemento atraves do indice
del bike[1]
print(bike)

# Desempilha o elemento da lista e adiciona-o a uma variavel
bikePoped=bike.pop()
print("poped = "+bikePoped)
print(bike)

# Ordenacao inversa
bike.reverse()
print(bike)

# Lista dentro de lista, lembrando que dessa forma ela se assemelha com o trabalho de ponteiros.
bike2=[]
bike2.append("blblbl")
bike2.append("13891iado")
bike2.append("qoq")
bike.append(bike2)
print(bike)
print(bike[4][2])
print("tamanho da lista = "+str(len(bike)))
print("tamanho da lista dentro da lista = "+str(len(bike[4])))
bike.append(1)
print(bike)
bike.sort()
print(bike)
bike2.append(52)
print(bike2)
print(bike)
bike2.sort()
print(bike)

# Retorna o valor do indice do elemento encontrado
print(bike.index("b"))
# Retorna erro pois o elemento nao se encontra na lista, mas sim na lista bike2
print(bike.index(52))