'''
TEM ALGUNS EXEMPLOS DE IMPUT na secao 05
para o python 2.7 e necessario utilizar input p/ numero e raw_input para string
pyhton 3 basta utilizar input
'''

# aceita apenas numero
teste = input("aceita apenas numero: ")
print(teste)

# aceita qualquer coisa
teste = raw_input("aceita qualquer coisa: ")
print(teste)

# teste input para entrada null
a = raw_input("teste input para entrada null: ")
print("------")
if not a:
    print("null")
else:
    print(a)
print("------")

# while 1
print("while basicao")
num = 1
while num <= 5:
    print(num)
    num += 1

# while + input, exemplo da secao 05
recheios_disponiveis = []
recheios_disponiveis.append("champignon")
recheios_disponiveis.append("azeite")
recheios_disponiveis.append("presunto")
recheios_disponiveis.append("pepperoni")
recheios_disponiveis.append("abacaxi")
recheios_disponiveis.append("borda de cheddar")

recheios_solicitados = []
recheio_pizza = []
pedido = raw_input("Adicione os ingredientes para a pizza: ")
while pedido:
    recheios_solicitados.append(str(pedido))
    pedido = raw_input("Adicione mais ingredientes ou pressione enter para finalizar: ")

for recheio_solicitado in recheios_solicitados:
    if recheio_solicitado in recheios_disponiveis:
        print("recheio " + recheio_solicitado + " adicionado com sucesso!")
        recheio_pizza.append(recheio_solicitado)
    else:
        print("recheio " + recheio_solicitado + " indisponivel no momento :(")
print("Pizza montada com os seguintes recheios:")
print(recheio_pizza)
print("----")

# while + input 2
prompt = "\nDigite uma cidade que voce quer visitar:"
prompt += "\n(Digite 'sair' quando quiser parar.) "

cidade = ""
while cidade != 'sair':
   cidade = raw_input(prompt)
   print("Eu adoraria visitar " + cidade.title() + "!")

# variavel sentinela
prompt = "\nDigite uma cidade que voce quer visitar:"
prompt += "\n(Digite 'sair' quando quiser parar.) "

ativo = True
while ativo :
   cidade = raw_input(prompt)
   if cidade == 'sair':
       ativo = False
   else:
       print("Eu adoraria visitar " + cidade.title() + "!")

# while com break
prompt = "\nDigite uma cidade que voce quer visitar:"
prompt += "\n(Digite 'sair' quando quiser parar.) "

while True:
   cidade = raw_input(prompt)
   if cidade == 'sair':
       break
   else:
       print("Eu adoraria visitar " + cidade.title() + "!")       

# usando continue para iteracao com while
print("Vamos imprimir todos os numeros impares entre 0 e 10 \nObs:E mais facil usar range!!")

numero_atual = 0
while numero_atual < 10:
   numero_atual += 1
   if numero_atual % 2 == 0:
      continue
   print(numero_atual)

# Comeca com uma lista de usuarios a serem confirmados
# e uma lista vazia de usuarios confirmados.
usuarios_nao_confirmados = ['alice', 'brian', 'candace']
usuarios_confirmados = []

# Verifica se ainda ha usuarios nao confirmados
# Move um usuario para a lista de confirmados
while usuarios_nao_confirmados:
    usuario_atual = usuarios_nao_confirmados.pop()
    print("Verificando o usuario: " + usuario_atual.title())
    usuarios_confirmados.append(usuario_atual)

# Mostra os usuarios confirmados
print("\nOs seguintes usuarios foram confirmados:")
for usuario_confirmado in usuarios_confirmados:
    print(usuario_confirmado.title())

# Remove todos os gatos da lista
animais = ['cachorro', 'gato', 'cachorro', 'peixinho', 'gato', 'coelho', 'gato']
print(animais)

while 'gato' in animais:
   animais.remove('gato')
  
print(animais)       