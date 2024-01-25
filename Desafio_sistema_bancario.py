menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0
saque_valor = 0


while True:
    opcao = input(menu)
    
    if opcao == 'd':
        deposito = int(input("informe o valor a ser depositado: "))
        
        if deposito < 0:
            print("digite um valor positivo")
        else:
            saldo = saldo + deposito
            print(f'Saldo atual: R${saldo:.2f}')
            extrato.append(f'Deposito: R${deposito:.2f}')
    
    elif opcao == 's':
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
        else:
            print("Você só pode sacar 3 vezes por dia")
        
    
    elif opcao == 'e':
        print(f'Valor total do saldo: R${saldo:.2f}')
        for item in extrato:
            print(item)
        
    
    elif opcao == 'q':
        break
        
    else:
        print("escolha uma das opções")