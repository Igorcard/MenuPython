import setuptools

def arquivoExiste(nomeArq):
    try:
        arquivo = open(nomeArq, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nomeArq):
    try:
        arquivo = open(nomeArq, 'wt+')
        arquivo.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo{nomeArq} criado com sucesso!')
    
def lerArquivo(nomeArq):
    try:
        arquivo = open(nomeArq, 'rt')
    except: 
        print('Erro ao abrir o arquivo!')
    else:
        print('PESSOAS CADASTRADAS')
        print(arquivo.readlines())
    finally:
        arquivo.close()
        
def cadastrarPessoa(nomeArq, nomePessoa='desconhecido', idade=0):
    try:
        arquivo = open(nomeArq, 'at')
    except: 
        print('Houve um ERRO na criação do arquivo!')
    else:
        try:
            arquivo.write(f'{nomePessoa};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nomePessoa} adicionado.')
            arquivo.close()
            