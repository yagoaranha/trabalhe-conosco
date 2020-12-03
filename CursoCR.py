import pandas as pd


df = pd.read_csv("teste2.csv",encoding="UTF-8", header=0)
class Cs:
    def __init__(self,curso):
        self.curso = curso

    def curso_solo(self):
        df_cs = df.loc[df['COD_CURSO'] == self.curso]
        if df_cs.COD_CURSO.any() == False:
            print("curso não existe!")
            return
        df_todos = pd.DataFrame(columns=['Curso', 'CR'])

        carga_total = sum(df_cs.CARGA_HORARIA)
        cr_aluno = sum(df_cs.NOTA * df_cs.CARGA_HORARIA / carga_total)
        df2 = pd.DataFrame([[self.curso, cr_aluno]], columns=['Curso', 'CR'])
        df_todos = df_todos.append(df2, ignore_index=True)
        print(df_todos)

    def curso_todos(self):
        df_todos = pd.DataFrame(columns=['Curso', 'CR'])
        for i in range(500):
            self.curso = self.curso + 1
            df_cr = df.loc[df['COD_CURSO'] == self.curso]

            if df_cr.MATRICULA.any() == True:
                carga_total = sum(df_cr.CARGA_HORARIA)
                cr_aluno = sum(df_cr.NOTA * df_cr.CARGA_HORARIA / carga_total)

                df2 = pd.DataFrame([[self.curso, cr_aluno]], columns=['Curso', 'CR'])
                df_todos = df_todos.append(df2, ignore_index=True)
        print(df_todos)



