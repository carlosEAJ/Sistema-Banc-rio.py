class Banco:
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0
        self.logado = False

    def deposito_func(self):
        deposito = int(input("Informe o valor a ser depositado: "))
        
        if deposito < 0:
            print("Digite um valor positivo")
        else:
            self.saldo += deposito
            print(f'Saldo atual: R${self.saldo:.2f}')
            self.extrato.append(f'Depósito: R${deposito:.2f}')
            return self.saldo

    def saque(self):
        LIMITE_SAQUES = 3
        if self.numero_saques < LIMITE_SAQUES:
            saque_valor = int(input("Informe o valor de saque: "))
            if saque_valor > 500: 
                print("Escolha um valor até R$500")
            else:
                if saque_valor > self.saldo:
                    print("Saldo insuficiente")
                elif saque_valor < 0:
                    print("Digite um valor positivo")
                else:
                    self.saldo -= saque_valor
                    self.numero_saques += 1  
                    print(f'O valor sacado atualmente foi de: R${saque_valor} e seu saldo atual é de: R${self.saldo}, você ainda pode sacar {LIMITE_SAQUES - self.numero_saques}')
                    self.extrato.append(f'Saque: R${saque_valor:.2f}')
                    return self.saldo, self.numero_saques
        else:
            print("Você só pode sacar 3 vezes por dia")  

    def extrato_func(self):
        print(f'Valor total do saldo: R${self.saldo:.2f}')
        for item in self.extrato:
            print(item)

    def usuario(self):
        self.nome = input("Informe seu nome: ")
        print(f'Bem vindo {self.nome}')
        return self.nome               

    def senha_func(self):
        senha = input("Informe sua senha: ")
        print(f'Bem vindo {self.nome}')
        return senha

    def login(self):
        self.usuario()
        self.senha_func()
        return self.nome

    @staticmethod
    def cpf():
        cpf = input("Informe seu CPF: ")
        if len(cpf) != 11:
            print("CPF inválido")
        else:
            return cpf

banco = Banco()

while True:
    
    if not banco.logado:
        banco.login()
        banco.logado = not banco.logado
        print("Bem vindo ao sistema")
        
    opcao = input(Banco.menu)
    
    if opcao == 'd':
        banco.deposito_func()
        
    elif opcao == 's':
        banco.saque()
        
    elif opcao == 'e':
        banco.extrato_func()
        
    elif opcao == 'q':
        break
        
    else:
        print("Escolha uma das opções")
