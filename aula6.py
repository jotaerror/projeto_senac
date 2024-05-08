# nome, idade, altura, tem_carro
'''
nome = input("Digite seu nome: ")
idade =  int(input("Digite sua idade:"))
altura = float(input("Digite sua altura: "))
tem_carro = input("Você possui algum carro? (Sim/Não): ")

tem_carro = tem_carro.lower() == "sim"

print("Informações digitadas: ")
print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura)
print("Tem carro? ", "Sim" if tem_carro else "Não")
'''
'''
def contagem_regressiva():
    numero = int(input("Digite um numero inteiro positivo: "))
    
    if numero <= 0:
        print("Digite um numero inteiro positivo. ")
        contagem_regressiva()
        
    else: 
        while numero >= 0:
            print(numero)
            numero -= 1 
            
    contagem_regressiva()
    
    '''
    
def soma (a, b):
    return a + b
def subtracao (a, b):
    return a - b
def multiplicacao (a, b):
    return a * b 
def divisao (a, b):
    if b!= 0:
        return a / b
    else:
        return "Divisao nao permitida" 
    
def calculadora ( ): 
    print("Bem-vindo a calculadora em Python!")
    print("Escolha a operacao desejada: ")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    
    escolha = input("Digite sua escolha 1/2/3/4: ")
    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro numero"))
        num2 = float(input("Digite o segundo numero"))
        
        if escolha == '1':
            print("Resultado", soma(num1, num2))
        elif escolha == '2':
            print("Resultado", subtracao(num1, num2))
        elif escolha == '3':
            print("Resultado", multiplicacao(num1, num2))
        elif escolha == '4':
            print("Resultado", divisao(num1, num2))
            
        else:
            print("Opcao invalida")
            
    calculadora()