import pandas as pd

df = pd.read_csv("teste2.csv",encoding="UTF-8", header=0)


class Cr:
    def __init__(self,matricula):
        self.matricula = matricula

    def matricula_todos(self):
        df_todos = pd.DataFrame(columns=['Matricula', 'CR'])
        for i in range(500):
            self.matricula = self.matricula + 1
            df_cr = df.loc[df['MATRICULA'] == self.matricula]

            if df_cr.MATRICULA.any() == True:
                carga_total = sum(df_cr.CARGA_HORARIA)
                cr_aluno = sum(df_cr.NOTA * df_cr.CARGA_HORARIA / carga_total)
                df2 = pd.DataFrame([[self.matricula, cr_aluno]], columns=['Matricula', 'CR'])
                df_todos = df_todos.append(df2, ignore_index=True)
        print(df_todos)
        return


    def matricula_solo(self):
        df_cr = df.loc[df['MATRICULA'] == self.matricula]

        if df_cr.MATRICULA.any() == False:
            print("Matricula não existe!")
            return


        df_todos = pd.DataFrame(columns=['Matricula', 'CR'])


        carga_total = sum(df_cr.CARGA_HORARIA)
        cr_aluno = sum(df_cr.NOTA * df_cr.CARGA_HORARIA / carga_total)

        df2 = pd.DataFrame([[self.matricula, cr_aluno]], columns=['Matricula', 'CR'])
        df_todos = df_todos.append(df2, ignore_index=True)
        print(df_todos)
        return









