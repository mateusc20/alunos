alunos = []
def cadastrar():
    print('Cadastrando')
    nome = input('Nome: ')
    turma = input('Turma: ')
    aluno = [nome, turma]
    #alunos.append(aluno)
    arquivo = open("alunos.txt", "a")
    arquivo.write(f"{nome},{turma}\n")
    arquivo.close()
    print('Cadastro realizado')

def listar():
    print('Listando')
    print('nome\tturma')
    for aluno in alunos:
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