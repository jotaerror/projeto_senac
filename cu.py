import sqlite3

class BancoDeDados:
    def __init__(self, nome_banco='banco.db'):
        self.nome_banco = nome_banco
        self.conn = sqlite3.connect(self.nome_banco)
        self.cursor = self.conn.cursor()
        self.configurar_banco()

    def configurar_banco(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contas (
                numero_conta TEXT PRIMARY KEY,
                nome_titular TEXT,
                saldo REAL
            )
        ''')
        self.conn.commit()

    def salvar_conta(self, numero_conta, nome_titular, saldo):
        self.cursor.execute('''
            INSERT OR REPLACE INTO contas (numero_conta, nome_titular, saldo) VALUES (?, ?, ?)
        ''', (numero_conta, nome_titular, saldo))
        self.conn.commit()

    def atualizar_saldo(self, numero_conta, saldo):
        self.cursor.execute('''
            UPDATE contas SET saldo = ? WHERE numero_conta = ?
        ''', (saldo, numero_conta))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()

class ContaBancaria:
    def __init__(self, nome_titular, numero_conta, saldo_inicial=0, banco_de_dados=None):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.banco_de_dados = banco_de_dados
        self.salvar_conta()

    def salvar_conta(self):
        self.banco_de_dados.salvar_conta(self.numero_conta, self.nome_titular, self.saldo)

    def atualizar_saldo(self):
        self.banco_de_dados.atualizar_saldo(self.numero_conta, self.saldo)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.atualizar_saldo()
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                self.atualizar_saldo()
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser maior que zero.")

    def consultar_saldo(self):
        return self.saldo

    def transferir(self, valor, outra_conta):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                self.atualizar_saldo()
                outra_conta.depositar(valor)
                print(f"Transferência de R${valor} para a conta {outra_conta.numero_conta} realizada com sucesso.")
            else:
                print("Saldo insuficiente para realizar a transferência.")
        else:
            print("O valor da transferência deve ser maior que zero.")

# Programa principal para testar a classe ContaBancaria e BancoDeDados
banco_de_dados = BancoDeDados()

conta1 = ContaBancaria("Manoel Gomi", "12345", banco_de_dados=banco_de_dados)
conta2 = ContaBancaria("Caneta Preta", "54321", 1000, banco_de_dados=banco_de_dados)

print("Saldo inicial da conta de Manoel gomi:", conta1.consultar_saldo())
print("Saldo inicial da conta de Caneta Preta:", conta2.consultar_saldo())

conta1.depositar(500)
conta1.sacar(200)
conta1.transferir(100, conta2)

print("Saldo atual da conta de Manoel Gomi:", conta1.consultar_saldo())
print("Saldo atual da conta de Caneta Preta:", conta2.consultar_saldo())

banco_de_dados.fechar_conexao()