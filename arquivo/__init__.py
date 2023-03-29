import setuptools

def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo{nome} criado com sucesso!')
    
def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except: 
        print('Erro ao abrir o arquivo!')
    else:
        print('PESSOAS CADASTRADAS')
        print(arquivo.readlines())