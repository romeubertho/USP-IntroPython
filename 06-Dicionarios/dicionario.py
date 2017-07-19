alien_0 = {
    "cor": "verde",
    "pontos": 10
}
# impressao divergente
print(alien_0)
print(alien_0.items())
print("----")
# imprime o valor da chave especifica
print(alien_0["cor"])
print(alien_0["pontos"])
print("----")


linguagem_favorita = {}
linguagem_favorita.__setitem__("paulo", "python")
linguagem_favorita.__setitem__("sara", "c")
linguagem_favorita.__setitem__("marcio", "ruby")
linguagem_favorita.__setitem__("vinicius", "go")
linguagem_favorita.__setitem__("joao", "mql5")
linguagem_favorita.__setitem__("edvaldo", "mql5")
linguagem_favorita.__setitem__("kenia", "c")
linguagem_favorita.__setitem__("mario", "python")
linguagem_favorita.__setitem__("junior", "python")
print(linguagem_favorita.items())

# iteracao com o dicionario parecido com oracle, precisa do item()
for nome, linguagem in linguagem_favorita.items():
    print("a linguagem do " + str(nome) + " e " + str(linguagem))
print("-----")

# iteracao apenas com as chaves
for nome in linguagem_favorita.keys():
    print(nome)
print("-----")

# iteracao apenas com as chaves
for nome in linguagem_favorita:
    print(nome)
print("----")
# ordena os itens atraves de suas respectivas chaves
print(sorted(linguagem_favorita.items()))
print("-----")

# ordena as chaves
print(sorted(linguagem_favorita.keys()))
print("-----")

# itera sobre os valores unicos
for linguagem in set(linguagem_favorita.values()):
    print(linguagem)

# imprime somente as chaves
print(alien_0.keys())

# remove a chave
print(alien_0.pop("cor"))
print(alien_0)

# adiciona a chave e inclusive atualiza ela
alien_0.__setitem__("cor", "verde")
print(alien_0)
alien_0.__setitem__("cor", "azul")
print(alien_0)

# Lista de dicionarios
aliens = []
for alien in range(0, 30):
    new_alien = {}
    new_alien.__setitem__("color", "green")
    new_alien.__setitem__("points", "5")
    new_alien.__setitem__("speed", "slow")
    aliens.append(new_alien)
    for x in range(0, 2):
        for alien in aliens[int(x):3+int(x)]:
            if alien["color"] == "yellow":
                alien.__setitem__("color", "red")
                alien.__setitem__("points", "15")
                alien.__setitem__("speed", "fast")
            elif(alien["color"]) == "green":
                alien.__setitem__("color", "yellow")
                alien.__setitem__("points", "10")
                alien.__setitem__("speed", "medium")
            

for alien in aliens[:10]:
    print(alien)

# Lista dentro de um diciionario

pizza = {
   'crust': 'thick',
   'toppings': ['mushrooms', 'extra cheese'],
   }
print("You ordered a " + pizza['crust'] + "-crust pizza " +
     "with the following toppings:")

for topping in pizza['toppings']:
   print("\t" + topping)  
