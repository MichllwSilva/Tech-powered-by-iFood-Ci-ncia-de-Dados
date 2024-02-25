# Tech powered by iFood | Ciência de Dados //
# Criar um Sistema Bancário Simples.  

menu = """

[d] depositar 
[s] sacar
[e] extrato
[q] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = input (menu)
    
    if opcao == "d":
        valor = float (input("informe o valor do deposito"))

        if valor > 0:
            saldo += valor
            extrato += f"depósito: R$ {valor:.2f}\n"

        else:
            print("operação falhou! O valor informado é inválido")

    elif opcao == "s":
        valor = float(input("informe o valor do saque:"))    

        excedeu_saldo = valor > saldo

        excedeu_limite = valor = limite

        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print ("operação falhou! você não tem saldo suficiente")

        elif excedeu_limite:
            print ("operação falhou! o valor do saque excede o limite.")   

        elif excedeu_saques:
            print ("operação falhou! numero máximo de saques excedidos")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("operação falhou! o valor informado é invalido")

    elif opcao =="e":
        print("\n===============EXTRATO================")      
        print("não foram realizdas movimentações." if not extrato else extrato)
        print(F'\nsaldo: R$ {saldo:.2f}')
        print("========================================")      

    elif opcao == "q":
        break            


    else: 
        print("operação inválidade, por favor selecione novamente a operação desejada")
            

                