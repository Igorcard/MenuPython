"""importa as funções de interface"""
from lib.interface import *


def arquivo_existe(nome_arq):
    """Esta função procura um arquivo e retorna se ele existe ou não"""
    try:
        arquivo = open(nome_arq, 'rt', encoding='utf-8')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome_arq):
    """Esta função cria um arquivo"""
    try:
        arquivo = open(nome_arq, 'wt+', encoding='utf-8')
        arquivo.close()
    except FileNotFoundError:
        print('Arquivo não encotnrado.')
    except PermissionError:
        print('Sem permissão para acessar o arquivo.')
    except IsADirectoryError:
        print('O caminho especificado é um diretório.')
    except UnicodeDecodeError:
        print('Erro de decodificação ao ler o arquivo')
    else:
        print(f'Arquivo{nome_arq} criado com sucesso!')

def ler_arquivo(nome_arq):
    """Esta função lê os dados contidos em um arquivo."""
    try:
        arquivo = open(nome_arq, 'rt', encoding='utf-8')
    except FileNotFoundError:
        print('Arquivo não encotnrado.')
    except PermissionError:
        print('Sem permissão para acessar o arquivo.')
    except IsADirectoryError:
        print('O caminho especificado é um diretório.')
    except UnicodeDecodeError:
        print('Erro de decodificação ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha_atual in arquivo:
            dado = linha_atual.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo.close()

def cadastrar_pessoa(nome_arq, nome_pessoa='desconhecido', idade=0):
    """Esta função cadastra uma pessoa com nome e idade em um arquivo."""
    try:
        arquivo = open(nome_arq, 'at', encoding='utf-8')
    except FileNotFoundError:
        print('Arquivo não encotnrado.')
    except PermissionError:
        print('Sem permissão para acessar o arquivo.')
    except IsADirectoryError:
        print('O caminho especificado é um diretório.')
    except UnicodeDecodeError:
        print('Erro de decodificação ao ler o arquivo')
    else:
        try:
            arquivo.write(f'{nome_pessoa};{idade}\n')
        except FileNotFoundError:
            print('Arquivo não encotnrado.')
        except PermissionError:
            print('Sem permissão para acessar o arquivo.')
        except IsADirectoryError:
            print('O caminho especificado é um diretório.')
        except UnicodeDecodeError:
            print('Erro de decodificação ao ler o arquivo')
        else:
            print(f'Novo registro de {nome_pessoa} adicionado.')
            arquivo.close()
            