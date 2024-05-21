'''import re

print("Cadastre aqui sua senha com os seguintes critérios: \n"
      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n")  
senha = input("Digite sua senha : ")

while not (re.search(r'.{8,}', senha) and   
           re.search(r'[A-Z]', senha) and 
           re.search(r'\d', senha) and   
           re.search(r'[!@#$%¨&*]', senha)):  
    senha = input("Use como base os critérios informado : ")

def buscaApelido(Agenda):
    apelido = input("Digite o apelido a procurar: ")
    for ele in Agenda:
        if ele["apelido"] == apelido:
            #print(f"nome completo = {ele['nome_completo']}")
            #print(f"Telefone fixo = {ele['fixo']}")
            #print(f"Telefone celular = {ele['celular']}")
            return ele
    agenda = []
contato = {}

while True:
    opcao = int(input(f"Digite 0 para inserir um novo contato: ") )  
    match opcao:

        case 0:
            contato = {}#sem isso, vai ficar tudo repetido...
            apelido = input("Digite o apelido: ")
            contato["apelido"] = apelido
            nome_completo = input("Digite o nome completo: ")
            contato["nome_completo"] = nome_completo
            fixo = input(" Digite o telefone fixo: ")
            contato["fixo"] = fixo
            celular = input("Digite o telefone celular: ")
            contato["celular"] = celular
            agenda.append(contato)
        case 2:#consultar um contato a partir do nome usual
            buscaApelido(agenda)
            if  buscaApelido(agenda):
                 print("Contato Inexistente")
            break


        case 3:#exibir a listagem de todos os contatos em ordem alfabética
            pass
        case 4:#sair
            break

agenda        



                            #LISTA INTELIGENTE#


escolha=5
lista=[]

while escolha !="0":
  print("Menu")
  print("0 - Fim")
  print("1 - Cadastra Produtos")
  print("2 - Confere Lista de Produtos")
  print("3 - Confirma Produto")
  print("4 - Mostra Total")
  escolha=input("Escolha uma opção:")
  if escolha =="0":
    escolha=input("Tem certeza que quer sair? 0 - Sim , 5 - Não")
  if escolha =="1":
    print("Cadastrando produto...")
    produto=input("Escolha o nome do produto:")
    quantidade=input("Escolha a quantidade do produto:")
    lista.append(["",produto,quantidade,0])
  if escolha=="2":
    print("Exibindo produtos...")
    contador=0
    for produto in lista:

      print(contador,"#",produto[0]," ",produto[1],"-",produto[2])
      contador=contador+1
  if escolha=="3":
    print("Confirmando produto...")
    posicao=input("Digite a posição do produto:")
    posicao_int=int(posicao)
    preco=input("Digite o preco do "+lista[posicao_int][1] +":")
    lista[posicao_int][0]="OK"
    lista[posicao_int][3]=preco
  if escolha=="4":
    print("Mostrando Todos Produtos...")
    print("Produtos que não foram comprados...")
    contador=0
    for produto in lista:
      if produto[0]=="":
        print(contador,"#",produto[0]," ",produto[1],"-",produto[2], "R$", produto[3])
        contador=contador+1
    print("Produtos que foram comprados...")
    contador=0
    precototal=0
    for produto in lista:
      if produto[0]=="OK":
        print(contador,"#",produto[0]," ",produto[1],"-",produto[2], "R$", produto[3])
        contador=contador+1
        precototal=precototal+int(produto[2])*float(produto[3])
    print("Preco Total: R$",precototal)


print("Fim do programa!")


                        #CONTADOR DE CARACTERES#






import math 

print("Calculadora de fatorial ! \ninstrucoes: \n 1- Digite o valor desejado \n 2 - Espere o resultado")
a = int(input("Digite o valor desejado"))
fatorial = math.factorial(a)
print("Resultado", fatorial)

                    #CALCULADORA DE FATORIAL#


crianca = adolescente = adulto = idoso = 0 
for n in range (5) : 
    idade = int(input("Digite a sua idade: "))
    
    if idade <13 :
        crianca = crianca + 1 
    elif 13<= idade < 13 :
        adolescente = adolescente + 1  
    elif 18<= idade < 60 :
        adulto =adulto + 1 
    else: 
        idoso = idoso + 1 
        
    print("crianças:" , crianca)
    print("adolescente:", adolescente)
    print("pessoas adultas:", adulto)
    print("Idoso:", idoso)'''
    
'''def fatorial(n):
      resultado =  1
      for in range (2, n+1):
        resultado*=i 
        
numero = int(input("Digite um numero inteiro: "))
print(f"Fatorial:", {numero} é de (fatorial(numero)))'''

'''# Crie uma lista vazia para armazenar os itens da lista de compras
lista_de_compras = []

# Loop principal para interagir com o usuário
while True:
    print("\n--- Lista de Compras ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista de compras")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        item = input("Digite o item que você deseja adicionar à lista de compras: ")
        lista_de_compras.append(item)
        print(f"'{item}' foi adicionado à lista de compras.")

    elif escolha == "2":
        if lista_de_compras:
            print("Itens na lista de compras:")
            for i, item in enumerate(lista_de_compras):
                print(f"{i + 1}. {item}")
            indice = int(input("Digite o número do item que você deseja remover: ")) - 1
            if 0 <= indice < len(lista_de_compras):
                item_removido = lista_de_compras.pop(indice)
                print(f"'{item_removido}' foi removido da lista de compras.")
            else:
                print("Índice inválido!")
        else:
            print("A lista de compras está vazia.")

    elif escolha == "3":
        if lista_de_compras:
            print("\nLista de compras:")
            for item in lista_de_compras:
                print("-", item)
        else:
            print("A lista de compras está vazia.")

    elif escolha == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")'''

