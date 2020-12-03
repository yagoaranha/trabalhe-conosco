from CR import Cr
from CursoCR import Cs



def Interface():
    sair = False
    while sair == False:
        dado = int(input('[0] para ver Menu de Cursos \n[1] para ver Menu de Alunos\n[2]Para sair\n'))
        if dado == 0:
            curinput = int(input('[0] Para Ver Todas os Cursos\n[1] Para ver Curso especifico\n'))
            if curinput == 0:
                a1 = Cs(0)
                a1.curso_todos()
                ext = int(input('Deseja sair?:\n[0] Sim\n[1]Não\n'))
                if ext == 0:
                    sair = True

            elif curinput == 1:
                x = int(input('Digite Codigo do Curso :'))
                a1 = Cs(x)
                a1.curso_solo()
                ext = int(input('Deseja sair?:\n[0] Sim\n[1]Não\n'))
                if ext == 0:
                    sair = True

            elif curinput != 1 or 0:
                print('Comando não Existe')
                ext = int(input('\nDeseja sair?:\n[0] Sim\n[1]Não\n'))
                if ext == 0:
                    sair = True

        if dado == 1:
            aluinput = int(input('[0] Para Ver Todas as Matriculas\n[1] Para ver Matricula especifica\n'))
            if aluinput == 0:
                a2 = Cr(0)
                a2.matricula_todos()
                ext = int(input('Deseja sair?:\n[0] Sim\n[1]Não\n'))
                if ext == 0:
                    sair = True

            elif aluinput == 1:
                y = int(input('Digite a Matricula do Aluno :'))
                a2 = Cr(y)
                a2.matricula_solo()
                ext = int(input('\nDeseja sair?:\n[0] Sim\n[1]Não\n'))
                if ext == 0:
                    sair = True

            elif aluinput != 1 or 0:
                print('Comando Não Existe'.format(aluinput))
                ext = int(input('\nDeseja sair?:\n[0] Sim\n[1]Não\n'))
                if ext == 0:
                    sair = True





