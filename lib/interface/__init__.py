"""Aqui conterá as funções para formatação"""
def leia_int(msg):
    """Esta função lê um dado informado pelo usuário e diz se ele é um número inteiro"""
    while True:
        try:
            variavel = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return variavel

def linha(tam = 42):
    """Esta função cria uma linha em string"""
    return '-' * tam

def cabecalho(txt):
    """Esta função cria um cabeçalho formatado em string"""
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    """Esta função apresenta as funcionalidades do programa"""
    cabecalho('\033[32mMENU PRINCIPAL\033[m')
    num_opcao = 1
    for item in lista:
        print(f'\033[33m{num_opcao}\033[m - \033[32m{item}\033[m')
        num_opcao += 1
    print(linha())
    opc = leia_int('\033[32mSua Opção: \033[m')
    return opc
