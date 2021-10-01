import clientes
from time import sleep

if __name__ == '__main__':
    clientes.cabecalho()
    while True:
        clientes.menu()
        opcao = clientes.valida_escolha('Digite uma opção: ')
        sleep(0.3)
        if opcao == 1:
            clientes.ver_cadastros()
        elif opcao == 2:
            clientes.cadastrar()
        else:
            clientes.sair_do_sistema()
            break
        sleep(0.3)
