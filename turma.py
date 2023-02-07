def cadastrar():
    print('Cadastrando')
    nome = input('Nome: ')
    turma = input('Turma: ')
    arquivo = open("alunos.txt", "a")
    arquivo.write(f"{nome},{turma}\n")
    arquivo.close()
    print('Cadastro realizado')

def listar():
    print('Listando')
    with open("alunos.txt", "r") as arquivo:
        print('nome\tturma')
        linhas = arquivo.readlines()
        for linha in linhas:            
            aluno = linha.strip().split(',')
            print(f'{aluno[0]}\t{aluno[1]}') 
              
while True:
    print('1. Cadastrar Aluno\n2. Listar\n3. Sair')
    opcao = int(input())
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    else:
        break
print('Até Mais!')