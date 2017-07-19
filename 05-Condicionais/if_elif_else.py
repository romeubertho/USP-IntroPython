carros = []
carros.append("audi")
carros.append("bmw")
carros.append("subaru")
carros.append("toyota")
carros.append("chevrolet")
carros.append("honda")

# if elif else
for carro in carros:
    if carro == "honda":
        print(carro.upper() + " !")
    elif carro == "BMW":
        print(carro.upper())
    elif carro == "toyota":
        print(carro.upper() + " !")
    else:
        print(carro.title() + " *")

print("------\n")

# multiplas condicionais
for x in range(0, int(len(carros))):
    if(carros[x] == "audi" and carros[x + 1] == "bmw"):
        print(str(x))
    if(carros[x] == "chevrolet" and carros[x + 1] == "honda"):
        print(str(x))

# mais condicionais

recheios_disponiveis = []
recheios_disponiveis.append("champignon")
recheios_disponiveis.append("azeite")
recheios_disponiveis.append("presunto")
recheios_disponiveis.append("pepperoni")
recheios_disponiveis.append("abacaxi")
recheios_disponiveis.append("borda de cheddar")

# teste input
a = raw_input()
print("------")
if not a:
    print("null")
else:
    print(a)
print("------")

# input com condicionais
recheios_solicitados = []
recheio_pizza = []
pedido = raw_input()
while pedido:
    recheios_solicitados.append(str(pedido))
    pedido = raw_input()

for recheio_solicitado in recheios_solicitados:
    if recheio_solicitado in recheios_disponiveis:
        print("recheio " + recheio_solicitado + " adicionado com sucesso!")
        recheio_pizza.append(recheio_solicitado)
    else:
        print("recheio " + recheio_solicitado + " indisponivel no momento :(")
print("Pizza montada com os seguintes recheios:")
print(recheio_pizza)
