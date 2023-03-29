from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'arquivo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Pessoas Cadastradas', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo do arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrarPessoa(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema.')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
    