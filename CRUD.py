def menu_fun():

    while menu != 5:

        print('### MENU ###')
        print('[1] Listar')
        print('[2] Cadastrar')
        print('[3] Atualizar')
        print('[4] Excluir')
        print('[5] Sair')
        print('### ----- ###')

    menu = int(input('Digite uma operação:'))
    if menu == 1:
        Listar()

    elif menu == 2:
        Cadastrar()

    elif menu == 3:

        Att()

    elif menu == 4:

        Deletar()
        Listar()

    elif menu == 5:
        print('Até a próxima')

    else:
        print('digite um número valido')


def Cadastrar():
    aluno['nome'] = str(input('Nome do aluno:'))
    aluno['idade'] = str(input('Idade do aluno:'))
    aluno['Turma'] = str(input('Turma do aluno:'))
    geral.append(aluno.copy())
    print('Aluno cadastrado com sucesso!')


def Listar():

    print('\nO ID é o primeiro indice da lista!\n')
    for i in enumerate(geral):
        print(i)


def Deletar():

    print('\nO ID é o primeiro indice da lista!\n')
    deletar = int(input('Didite o Id que vc deseja deletar:'))
    geral.pop(deletar)
    print('Usuario deletado com sucesso')


def Att():
    atualizar = int(input('Id do aluno que você deseja atualizar:'))

    nome = str(input('Nome do aluno:'))
    idade = str(input('Idade do aluno:'))
    turma = str(input('Turma do aluno:'))

    geral[atualizar].update({'nome': nome, 'idade': idade, 'turma': turma})
    print('Atualizado com sucesso')
    for i in enumerate(geral):
        print(i)


def prosseguir():
    resp = int(input("Voce deseja continuar? 1 para sim 2 para não:"))

    if resp == 1:
        return menu()
    else:
        print("Terminado")


if __name__ == '__ __':
    aluno = dict()
    geral = list()
    menu = 0
