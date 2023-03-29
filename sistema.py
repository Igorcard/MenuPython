"""Sistema principal do menu"""
from time import sleep
from lib.arquivo import ler_arquivo, arquivo_existe, cadastrar_pessoa, criar_arquivo
from lib.interface import menu, cabecalho, leia_int

ARQUIVO = 'arquivo.txt'

if not arquivo_existe(ARQUIVO):
    criar_arquivo(ARQUIVO)

while True:
    RESPOSTA = menu(['Pessoas Cadastradas', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if RESPOSTA == 1:
        #Opção de listar o conteúdo do arquivo.
        ler_arquivo(ARQUIVO)
    elif RESPOSTA == 2:
        #Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        NOME = str(input('Nome: '))
        IDADE = leia_int('Idade: ')
        cadastrar_pessoa(ARQUIVO, NOME, IDADE)
    elif RESPOSTA == 3:
        cabecalho('Saindo do sistema.')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
    