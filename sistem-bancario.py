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

while True:

    opcao = input(menu)
    opcao = opcao.upper()#Caso o usuário digite a letra D minúscula, o sistema transforma ela em maiúscula.

    match opcao: #Utilizei a estrutura MATCH CASE (Switch Case em outras linguagens), para uma melhor organização dos blocos de código!
        case "D":
            print("Depósito\n")
            valor_dep = float(input("Digite o valor à depositar: "))
            if valor_dep > 0: #Verifica se o valor à ser depositado é maior que 0!
                saldo = saldo + valor_dep #Serve para somar o valor depositado ao saldo já existente!
                resumo_dep = f"Depósito de R$ {valor_dep}" #É o resumo da operação que será inserido no Extrato!
                extrato.append(resumo_dep) #Serve para adicionar o valor depositado ao extrato!
                print(f"Foi depositado o valor de R$ {valor_dep}")
            else:
                print("O valor precisa ser maior do que 0!")

        case "S":
            print("Saque\n")
            if numero_saques < LIMITE_SAQUES:
                valor_saque = float(input("Digite o valor que deseja sacar: "))
                if valor_saque > 0: #Verifica se o valor a ser sacado é maior que 0!
                    if valor_saque <= saldo: #Verifica se o valor a ser sacado é menor ou igual ao saldo!
                        if valor_saque <= limite: #Verifica se o valor a ser sacado é menor ou igual ao limite de saque (500 reais)! 
                            saldo = saldo - valor_saque #Serve para diminuir o valor sacado do saldo já existente!
                            resumo_saque = f"Saque de R$ {valor_saque}" #É o resumo da operação que será inserido no Extrato!
                            extrato.append(resumo_saque) #Serve para adicionar o valor sacado ao extrato!
                            numero_saques += 1 #Serve para adicionar 1 ao número de saques já realizados!
                            print(f"Foi feito um saque de R$ {valor_saque}")
                        else:
                            print("O valor excede o limite por saque!")
                    else:
                        print("O seu saldo é inferior ao valor que deseja sacar!")
            else:
                print("Você excedeu o limite de 3 saques diários!")

        case "E":
            print("======================= Extrato =======================")
            tamanho_extrato = len(extrato) #Serve para contar o número de elementos na lista "Extrato"
            if tamanho_extrato > 0: #Serve para verificar se o número de elementos na lista "Extrato" é maior que 0!
                for movimento in extrato: #Serve para percorrer todos os elementos na lista "Extrato", e exibi-los.
                    print(f"Foi feito um {movimento}")
            else:
                print("Não houveram movimentações de Depósito ou Saque!")
            print(f"\nO seu saldo atual é de R${saldo}")
            print("=======================================================")

        case "Q":
            print("Saindo do Programa")
            break