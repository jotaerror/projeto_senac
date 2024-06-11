#################################################################################

# Sistema genérico de estoque utilizando Programação a Objetos e o SGBD SQLite

#################################################################################

import sqlite3


class ItemEstoque:
    def __init__(self, nome, marca, modelo, preco, quantidade):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.quantidade = quantidade
        
        
def exibir_informacoes(self):
    print(f"Nome: {self.nome}\nMarca: {self.marca}\nModelo: {self.modelo}\nPreço: R$ {self.preco}\nQuantidade: {self.quantidade}")
    
class Estoque:
    def __init__(self, db_name="estoque.db" ):
        self.conn = sqlite3.connect(db_name)
        self.criar_tabela()
        
# Essa função cria a tabela      
def criar_tabela(self):
    with self.conn: 
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY
                nome TEXT NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                preco REAL NOT NULL
                quantidade INTEGER NOT NULL 
            )
                          
                          
        """)

# Essa função adiciona um item        
def inserir_item(self, nome_item):
    item = ItemEstoque.objects.get
    with self.conn:
        self.conn.execute("""
            INSERT INTO itens (nome, marca, modelo, preco, quantidade)
            VALUES (?,?,?,?,?)""", (item.nome, item.marca, item.modelo, item.preco, item.quantidade))
    print("Item adicionado ao estoque com sucesso!")
    

# Essa função remove algum item
def remover_item(self, nome_item):
    with self.conn:
        cursor = self.conn.execute("DELETE FROM itens WHERE nome =?", (nome_item,))
    if cursor. rowcount > 0:
        print("Item removido do estoque com sucesso!") 
    else: 
        print("Item não encontrado!")
    
    
#Essa função irá editar um item
def editar_item(self, nome_item):
    with self.conn:
        cursor = self.conn.execute("SELECT * FROM itens WHERE nome =?", (nome_item,))
        for linha in cursor:
            print(f"Nome: {linha[1]}\nMarca: {linha[2]}\nModelo: {linha[3]}\nPreço: R$ {linha[4]}\nQuantidade: {linha[5]}")
            novo_nome = input("Digite o novo nome do item: ")
            novo_marca = input("Digite a nova marca do item: ")
            novo_modelo = input("Digite o novo modelo do item: ")
            novo_preco = input(float("Digite o novo preço do item: "))
            novo_quantidade = input(int("Digite a nova quantidade do item: "))
        

#Essa função irá exibir todos os itens do estoque
def exibir_itens(self):
    with self.conn:
        cursor = self.conn.execute("SELECT * FROM itens")
        for linha in cursor:
            print(f"Nome: {linha[1]}\nMarca: {linha[2]}\nModelo: {linha[3]}\nPreço: R$ {linha[4]}\nQuantidade: {linha[5]}")