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

                for i in geral:
                    print(i)

            elif menu == 2:
                aluno['ID'] = int(input('ID do aluno:'))
                aluno['nome'] = str(input('Nome do aluno:'))
                aluno['idade'] = str(input('Idade do aluno:'))
                aluno['Turma'] = str(input('Turma do aluno:'))
                geral.append(aluno.copy())
                print('Aluno cadastrado com sucesso!')

            elif menu == 3:
                print('')

            elif menu == 4:
                print('nada ainda')
                print(menu)

            elif menu == 5:
                print('num')
            else:
                print('digite um número valido')









