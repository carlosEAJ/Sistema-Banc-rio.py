menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

saldo = 0
extrato = []
numero_saques = 0
logado = False


def deposito_func(saldo):
            deposito = int(input("informe o valor a ser depositado: "))
            
            if deposito < 0:
                print("digite um valor positivo")
            else:
                saldo = saldo + deposito
                print(f'Saldo atual: R${saldo:.2f}')
                extrato.append(f'Deposito: R${deposito:.2f}')
                return saldo

def saque(numero_saques, saldo, extrato):
            LIMITE_SAQUES = 3
            if numero_saques < LIMITE_SAQUES:
                saque_valor = int(input("informe o valor de saque: "))
                if saque_valor > 500: 
                    print("Escolha um valor até R$500")
                else:
                    if saque_valor > saldo:
                        print("Saldo insuficiente")
                    elif saque_valor < 0:
                        print("Digite um valor positivo")
                    else:
                        saldo -= saque_valor
                        numero_saques += 1  
                        print(f'O valor sacado atualmente foi de : R${saque_valor} e seu saldo atual é de: R${saldo}, você ainda pode sacar {LIMITE_SAQUES - numero_saques}')
                        extrato.append(f'Saque: R${saque_valor:.2f}')
                        return saldo, numero_saques
            else:
                print("Você só pode sacar 3 vezes por dia")  

def extrato_func(saldo, extrato):
            print(f'Valor total do saldo: R${saldo:.2f}')
            for item in extrato:
                print(item)

def usuario():
    nome = input("Informe seu nome: ")
    return nome               

def senha_func(nome):
    senha = input("Informe sua senha: ")
    print(f'Bem vindo {nome}')
    return senha

def login():
    nome = usuario()
    senha_func(nome)

def cpf():
    cpf = input("Informe seu cpf: ")
    if cpf > 11:
        print("cpf invalido")
    else:
        return cpf

while True:
    
    if not logado:
        login()
        logado = not logado
        print("Bem vindo ao sistema")
    opcao = input(menu)
    if opcao == 'd':
        saldo = deposito_func(saldo)
    elif opcao == 's':
       saldo, numero_saques =  saque(numero_saques, saldo, extrato)
    
    elif opcao == 'e':
        extrato_func(saldo, extrato)
    
    elif opcao == 'q':
        break
        
    else:
        print("escolha uma das opções")