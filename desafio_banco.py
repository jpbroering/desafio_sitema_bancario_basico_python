MENSAGEM = """\n\n################################################################################
                        Bem vindo ao Banco sem nome!
################################################################################
Digite para:
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair
################################################################################

opção: """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0

movimentacao = False

LIMITE_DE_SAQUES = 3

extrato = """
"""

while True:
    opcao = input(MENSAGEM)

    if opcao == "d":
        while True:
            opcao = input("\nCaso deseje proseguir com deposito digite [d], se deseja sair, digite [q]: ")

            if opcao == "d":
                deposito = float(input("\nDigite o valor a ser depositado: "))

                if deposito > 0:
                    saldo += deposito
                    mensagem_saida = f"R$ {deposito:.2f} depositados.\n\n"

                    movimentacao = True
                    extrato += mensagem_saida.strip().center(80)+"\n\n"
                    print("\n\n"+mensagem_saida)

                else:
                    print("Digite um número positivo válido!")
            elif opcao == "q":
                break
            else:
                print("\n\nSelecione uma opção válida.")

    elif opcao == "s":
        while True:
            opcao = input("\nCaso deseje proseguir com saque digite [s], se deseja sair, digite [q]: ")
            if opcao == "s":
                saque = float(input("\nDigite o valor a ser sacado: "))

                excedeu_saldo = saque > saldo

                excedeu_limite = saque > limite

                excedeu_saque = numero_de_saques >= LIMITE_DE_SAQUES

                if excedeu_saldo:
                    print("\nNão será possivél sacar o dinheiro por saldo insuficiente.")

                elif excedeu_limite:
                    print(f"\nNão será possivél sacar o dinheiro por ultrapassar o limite de {limite}.")

                elif excedeu_saque:
                    print(f"\nNão será possivél sacar o dinheiro por ultrapassar o limite de {LIMITE_DE_SAQUES} saques diários.")

                elif saque > 0:
                    numero_de_saques += 1
                    saldo -= saque
                    mensagem_saida = f"R$ {saque:.2f} sacados.\n\n"

                    movimentacao = True
                    extrato += mensagem_saida.strip().center(80)+"\n\n"
                    print("\n\n"+mensagem_saida)

                else:
                    print("\nDigite um número positivo válido!")
            elif opcao == "q":
                break
            else:
                print("\n\nSelecione uma opção válida.")

    elif opcao == "e":
        while True:
            opcao = input("\nExtrato selecionado! Caso deseje proseguir digite [e], se deseja sair, digite [q]: ")

            if opcao == "e":
                extrato += f"Saldo atual da conta: R$ {saldo:.2f}".strip().center(80)
                print(" EXTRATO ".center(80,"#"), end="\n\n")
                print(extrato if movimentacao == True else "Nenhuma movimentação realizada.".strip().center(80)+"\n\n"+f"Saldo atual da conta: R$ {saldo:.2f}".strip().center(80))
                print("################################################################################")
            elif opcao == "q":
                break
            else:
                print("\n\nSelecione uma opção válida.")

    elif opcao == "q":
        print("\n\nObrigado por utilizar nossos serviços!")
        break

    else:
        print("\n\nSelecione uma opção válida.")