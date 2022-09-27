def Cadastrar():

    aluno['nome'] = str(input('Nome do aluno:'))
    aluno['idade'] = str(input('Idade do aluno:'))
    aluno['Turma'] = str(input('Turma do aluno:'))
    geral.append(aluno.copy())

def Listar():
    print('\nId é o número antes de nome!\n' )
    for i in enumerate(geral):
        print(i)


def Deletar():
    print('\nId é o número antes de nome!\n' )
    deletar = int(input('Didite o Id que vc deseja deletar:'))
    geral.pop(deletar)
    print('Usuario deletado com sucesso')

def Att():

    print('\nId é o número antes de nome!\n' )
    atualizar = int(input('Id do aluno que você deseja atualizar:'))

    nome = str(input('Nome do aluno:'))
    idade = str(input('Idade do aluno:'))
    turma = str(input('Turma do aluno:'))

    geral[atualizar].update({'nome': nome, 'idade': idade, 'turma': turma})
    print('Atualizado com sucesso')
    for i in enumerate(geral):
        print(i)


if __name__ == '__main__':
        aluno = dict()
        geral = list()
        menu = 0



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
                print(Listar())

            elif menu == 2:
                print(Cadastrar())
                print('Aluno cadastrado com sucesso!')


            elif menu == 3:

                print(Att())


            elif menu == 4:

                print(Deletar())
                print(Listar())

            elif menu == 5:
                print('Até a próxima')

            else:
                print('digite um número valido')









