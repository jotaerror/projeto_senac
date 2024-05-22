class Pessoa:
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
print(pessoa1)
