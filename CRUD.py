if __name__ == '__main__':
        aluno = dict()
        geral = list()


        indice = 0
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

                aluno['ID'] = indice
                aluno['nome'] = str(input('Nome do aluno:'))
                aluno['idade'] = str(input('Idade do aluno:'))
                aluno['Turma'] = str(input('Turma do aluno:'))
                geral.append(aluno.copy())
                print('Aluno cadastrado com sucesso!')
                indice += 1

            elif menu == 3:
                atualizar = int(input('Indece do aluno que você deseja atualizar:'))
                


            elif menu == 4:
                deletar = int(input('Didite o Id que vc deseja deletar:'))
                geral.pop(deletar)
                print('Usuario deletado com sucesso')

            elif menu == 5:
                print('Até a próxima')
            else:
                print('digite um número valido')









