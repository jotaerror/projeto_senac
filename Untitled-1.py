'''class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        
    
    def Envelhecer(self):
        self.idade = self.idade + 1
        print(f"Sua idade está {self.idade}.")
        if self.idade < 21:
           self.crescer(0.5)
            
    def Engordar(self, peso):
        self.peso = self.peso + 1
        print(f"Seu peso está {self.peso}.")
            
    def Emagrecer(self):
        self.peso = self.peso - 1
        print(f"Seu peso está {self.peso}.")
        
    def crescer(self, altura):
        self.altura += altura
        
    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nAltura: {self.altura}\nPeso: {self.peso}\n"
    
pessoa1 = Pessoa("Junior", 20, 65, 167)

print("Dados iniciais")

print(pessoa1)

pessoa1.Envelhecer()

pessoa1.Engordar(10)

print("Dados após envelhecer e engordar: ")
print(pessoa1)'''



'''class Criar_conta():
    def __init__(self, titular, conta, saldo):
        self.titular =  titular
        self.conta = conta
        self.saldo = saldo
        
    def Deposita(conta):
        self.saldo += self.saldo 
        print(f"Seu saldo está {self.saldo}.")
        
    def Saca(conta, valor):
        self.saldo = self.saldo 
        print(f"Seu saldo é de {self.saldo}.")
        
    def Tranferecencia(self, saldo):
        self.saldo -= self.saldo 
        print(f"Seu saldo é de {self.saldo}.")
        
Criar_conta1 = Criar_conta("Junior", "0999", "5000")

print("Dados iniciais")

print(Criar_conta).Deposita(500)

Criar_conta.Deposita(500)

Criar_conta.Saca(500)

Criar_conta.Tranferecencia(500)

print("Dados após depositar, sacar e tranferir: ")'''

#FEITO POR EU MESMO#
'''
class ContaBancaria:
    
    def __init__(self, numero, titular, saldo=0, limite=0):
        
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    
    def sacar(self, valor):
        print("\nRealizando saque...")
        if (self.saldo - valor) < 0:  
            print(f"Saque não realizado {self.titular}, dinheiro insuficiente na conta")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado, agora seu saldo é de R${self.saldo}")
    
    # Método para depositar um certo valor
    def depositar(self, valor):
        print("\nRealizando depósito...")
        self.saldo += valor
        print(f"Deposito de R${valor} realizado, agora seu saldo é de R${self.saldo}\n")
    
    
    def extrato(self):
        print("\nColetando extrato...")
        print(f"Seu saldo atual é de R${self.saldo}")
        
    def transferir(self,valor):
        print("\ntransferindo valores...")
        if self.saldo <= 0:
            print(f"Transferencia não realizada {self.titular}, saldo insuficiente na conta")
        else:
            self.saldo >= 1 
            print(f"Transferencia de R${valor} realizada, agora seu saldo é de R${self.saldo}")
            
    def extrato(self):
        print("\nColetando extrato...")
        print(f"Seu saldo atual é de R${self.saldo}")
            
            
conta1 = ContaBancaria(111, "Junior")
conta1.extrato()
conta1.sacar(200)
conta1.depositar(250)
conta1.transferir(200)
conta1.extrato()'''

#FEITO PELO PROFESSOR#

class ContaBancaria:
    
    def __init__(self, nome_titular, numero_conta, saldo_inicial=0):
    
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo_inicial = saldo_inicial
        
    def depositar(self, valor):
        if valor < 0 : 
            print("Valor de deposito inválido")
        else:
            self.saldo += valor 
            print(f"Deposito de R${valor} realizado, agora seu saldo é de R${self.saldo}")
            
    def sacar(self, valor):
        if valor > 0: 
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                print(f"Saque não realizado {self.nome_titular}, dinheiro insuficiente na conta")
        else:
            print("Valor de saque invalido")
    def consultar_saldo(self):
        return self.saldo
    
    def tranferir(self, outra_conta):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                outra_conta.depositar(valor) 
                print("Tranferencia feita com sucesso")
            else:
                print("Você não possui saldo")
        else:
            print("Valor da transferencia deve ser maior que 0")
            