def cadastrar ():
        print('Cadastrando')

def listar ():
        print('Listando')

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