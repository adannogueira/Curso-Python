from time import sleep


class OutOfRangeError(ValueError):
    pass


def valida_escolha(msg):
    while True:
        try:
            escolha = int(input(msg))
            if not 1 <= escolha <= 3:
                raise OutOfRangeError()
            return escolha
        except TypeError:
            print('\033[31mERRO: Digite um número inteiro.\033[m')
        except KeyboardInterrupt:
            sair_do_sistema()
            return True
        except OutOfRangeError:
            print('\033[31mERRO: Digite um número da lista.\033[m')
        except ValueError:
            print('\033[31mERRO: Você precisa digitar um número.\033[m')


def cabecalho():
    print('-' * 35)
    sleep(0.1)
    print(f'\033[34m{"SISTEMA DE CADASTRO":^35}')
    sleep(0.1)
    print(f'{"DE CLIENTES":^35}\033[m')


def menu():
    print('-' * 35)
    sleep(0.1)
    print(f'{"MENU PRINCIPAL":^35}')
    sleep(0.1)
    print('-' * 35)
    sleep(0.1)
    print('1 - \033[34mVer pessoas cadastradas\033[m')
    sleep(0.1)
    print('2 - \033[34mCadastrar nova pessoa\033[m')
    sleep(0.1)
    print('3 - \033[34mSair do sistema\033[m')
    sleep(0.1)
    print('-' * 35)


def ver_cadastros():
    print('-' * 35)
    sleep(0.1)
    print(f'{"Exibindo Cadastros":^35}')
    sleep(0.1)
    print('-' * 35)
    try:
        file = open('clientes.txt', 'r')
    except FileNotFoundError:
        file = open('clientes.txt', 'w+')
    linha_a_linha(file)
    file.close()


def cadastrar():
    print('-' * 35)
    sleep(0.1)
    print(f'{"Cadastrar Pessoa":^35}')
    sleep(0.1)
    print('-' * 35)
    sleep(0.1)
    try:
        file = open('clientes.txt', 'a')
        nome = input('Digite o nome: ')
        sleep(0.1)
        idade = leiaInt(input('Digite a idade: '))
        file.write(f'{nome} : {idade}\n')
        file.close()
        sleep(0.1)
        print('Pessoa cadastrada com sucesso.')
        sleep(0.2)
    except:
        print('Erro ao abrir o arquivo')


def sair_do_sistema():
    print('-' * 35)
    sleep(0.1)
    print(f'{"Saindo do Sistema":^35}')
    sleep(0.1)
    print('-' * 35)


def leiaInt(numero):
    while 1:
        try:
            return int(numero)
        except ValueError:
            print('\033[7mDigite um número inteiro válido.\033[m')
            sleep(0.2)
            numero = input('Digite a idade: ')


def linha_a_linha(txt):
    texto = []
    linha = txt.readline()
    while linha:
        texto.append(linha.replace('\n', '').split(' : '))
        linha = txt.readline()
    print(f'{"Nome":<30}{"Idade":>5}')
    print('-' * 35)
    for c in range(len(texto)):
        print(f'{texto[c][0]:<30}{texto[c][1]:>5}')
