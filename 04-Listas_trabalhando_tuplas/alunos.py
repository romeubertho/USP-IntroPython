alunos = []
alunos.append("Maria")
alunos.append("Joao")
alunos.append("Lucas")
alunos.append("Marcos")
alunos.append("Edson")
alunos.append("Carlos")
alunos.append("Thomas")
print(alunos)
# outra forma de utlizar o for
for aluno in alunos:
    print(aluno)
# Imprime os valores conforme a regra
for value in range(0, 5):
    print(value)
for valueImpar in range(1, 15, 2):
    print("valor impar = " + str(valueImpar))
for valuePar in range(0, 15, 2):
    print("valor par = " + str(valuePar))

# Atribui a variavel os valores conforme a regra    
numeros = list(range(1,10))
numerosImpares = list(range(1,15,2))
numerosPares = list(range(0,15,2))
print(numeros)
print(numerosImpares)
print(numerosPares)

# Quadrados recebe x^2 onde x varia de 1-11
quadrados=[]
for valor in range(1,11):
    quadrados.append(valor**2)
print(quadrados)
# Extrai informacoes aritmeticas da lista
print("Min = "+str(min(quadrados)))
print("Max = "+str(max(quadrados)))
print("Sum = "+str(sum(quadrados)))
print("Mean = "+str(sum(quadrados)/len(quadrados)))

# Printa os quadrados de n:m
print(quadrados[:])
print(quadrados[:11])
print(quadrados[8:11])
print(quadrados[:5])
print(quadrados[5:])

# Ordena alunos e printa apenas os 3 primeiros alunos
alunos.sort()
for aluno in alunos[:3]:
    print("um dos 3 primeiros alunos em ordem alfabetica: "+aluno)

# cubos recebe x^3 onde x varia de 1-9
cubos = [valor**3 for valor in range(1,9)]
print(cubos)

#copia lista sem slice, aqui funciona como se estivesse trabalhando com ponteiros
print("copy sem slice")
cubos2=cubos
print(cubos2)
cubos2.append(7878)
cubos.append(199)
print(cubos)
print(cubos2)
cubos.remove(7878)
cubos.remove(199)

#copia lista com slice, aqui a copia funciona normal, sem utilizacao de ponteiros 
print("copy com slice")
cubos2=cubos[:]
print(cubos2)
cubos2.append(5567)
cubos.append(4365)
print(cubos)
print(cubos2) 

# Tanto faz utilizar [] ou ()
dimensions = [200,50]
print("dimensions original :")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("dimensions modificada :")
for dimension in dimensions:
    print(dimension)

 # Read an integer:
a = input()
cubo=[]
for valor in range(1,int(a)+1):
    cubo.append(valor**3)
print(sum(cubo))
      