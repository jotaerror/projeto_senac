'''def primo(num):
    if num <= 1:
        return False 
    elif num == 2:
    return True
    elif num % 2 == 0 or num % 3 == 0 :
        return False   
    i = 5 
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
    
    
ano = int(input('Ano: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')
    
def criar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    invertido = texto[::-1]
    
    if texto == invertido:
        return True
    else:
        return False

entrada = input("Digite uma palavra ou frase: ")
if criar_palindromo(entrada):
    print("A entrada é um palíndromo!")
else:
    print("A entrada não é um palíndromo!")
    

c = float(input("Digite a temperatura em Celsius:"))
f = 32 + (9/5)*c
print("A temperatura em Celsius é:",c,"°C")
print("A temperatura em Fahrenheit é:",f,"°F")

a = int(input("Digite algum valor: "))
b = int(input("Digite algum valor: "))
c = int(input("Digite algum valor: "))
d = int(input("Digite algum valor: "))
e = int(input("Digite algum valor: "))

f =  a + b + c + d + e
g = f / 5
print(" o valor e ", g)

a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))
    
if (a + b < c) or (a + c < b) or (b + c < a):
        print('Nao é um triangulo')
elif (a == b) and (a == c) :
        print('Equilatero')
elif (a==b) or (a==c) or (b==c):
        print('Isósceles')
else:
        print('Escaleno')'''
        
'''def contador_vogais(word):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in vogais : 
        if char in vogais : 
            count*=1
    return count
    
    word = input("Digite uma palavra: ")
    contador_geral = contador_vogais(word)
    print("A palavra", word, "contém, contador_geral, "vogais")
    

palavra = "abecedario";
assert 6 == contarVogais(palavra)'''


'''from random import choice
import string

tamanho_da_senha = int(input("Quantos dígitos você quer na sua senha? "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha_segura = ''
for i in range(tamanho_da_senha):
    senha_segura += choice(caracteres)

print("A senha (segura) gerada é: ",senha_segura)'''