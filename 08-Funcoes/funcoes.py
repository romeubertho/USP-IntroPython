# Funcao hello()
def hello():
    print("Hello!")

# funcao hello() com args
def hello1(name):
    print("Hello "+name+"!")
hello()
hello1("Juca")

# funcao teste() passando os argumentos com palavra chave
def teste(a,b):
    print("a = "+str(a))
    print("b  = "+str(b))
teste(1,2)
teste(b=2,a=1)

# funcao teste() com valor padrao
def teste(a=0,b=1):
    print("a = "+str(a))
    print("b  = "+str(b))
teste()
teste(5)

# funcao que retorna valores
def sum(a=0,b=0):
    return a+b
print(sum(5,3))

# funcao que retorna se o numero e par ou nao
def par_impar(num):
    if num % 2 == 0:
        return 1
    else:
        return 0
print(par_impar(1))
print(par_impar(2))

# funcao que adiciona uma chave no dicionario
def add(dic,key,value):
    dic.__setitem__(key,value)
    return dic
dicionario={}
print(add(dicionario,"key","value"))
print(add(dicionario,"key2","value2"))
print(add(dicionario,"key3","value3"))

# modificando listas dentro de uma funcao
def print_models(unprinted_designs, completed_models):
   """
   Simulate printing each design, until there are none left.
   Move each design to completed_models after printing.
   """
   while unprinted_designs:
       current_design = unprinted_designs.pop()
  
       # Simulate creating a 3d print from the design.
       print("Printing model: " + current_design)
       completed_models.append(current_design)
      
def show_completed_models(completed_models):
   """Show all the models that were printed."""
   print("\nThe following models have been printed:")
   for completed_model in completed_models:
       print(completed_model)
      
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print("designs nao impressos: ")
print(unprinted_designs)
print("\n")

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# funcao com numero arbitrario de args
def make_pizza(*ingredientes):
    print("\nFazendo uma pizza com "+str(len(ingredientes))+" ingredientes")
    for ingrediente in ingredientes:
        print(" - "+ingrediente)

make_pizza("gorgonzola","tomate seco","pepperoni","catupiry")

# funcao com argumentos de palavra chave arbitrarios
def build_profile(first, last, **user_info):
   """Build a dictionary containing everything we know about a user."""
   profile = {}
   profile['first_name'] = first
   profile['last_name'] = last
   for key, value in user_info.items():
       profile[key] = value
   return profile



user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print("\n")                            
print(user_profile)