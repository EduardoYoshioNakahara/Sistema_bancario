import os


i = True
saldo = 1000
while(i == True):
    os.system('cls')
    mensagem = print("""
*****************************************************
***************seja bem-vindo ao bank****************
*****************************************************
""")
    menu = print('''
             1 - sacar
             2 - depositar
             3 - visualizar extrato
             0 - sair
             ''')
    opcao = int(input('insira a opção desejada: '))
    if (opcao == 1):
        valor_sacar  = float(input('insira o valor que deseja sacar: '))
        saldo -= valor_sacar
        
    elif (opcao == 2):
        valor_depositar = float(input('insira o valor que deseja depositar: '))
        saldo += valor_depositar
    elif (opcao == 3):
        print(f'Seu saldo é R${saldo}')
        input('aperte enter para sair')
    elif (opcao == 0):
        print('saindo..')
        break