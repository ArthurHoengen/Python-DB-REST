import sqlite3
from banco import Banco


class Funcionarios:
    def __init__(self):
        self.banco = Banco()

    def select_funcionarios(self):
        try:
            lista = []
            c = self.banco.conexao.cursor()

            c.execute("select * from funcionarios")

            record = c.fetchall()

            for linha in record:
                lista.append(
                    {
                        "id": linha[0],
                        "nome": linha[1],
                        "sexo": linha[2],
                        "data de nascimento": linha[3],
                        "quantidade de dependentes": int(linha[4]),
                        "cargo": linha[5],
                        "salario": int(linha[6]),
                        "id do setor": int(linha[7]),
                    }
                )

            c.close()

            return True, lista
        except sqlite3.Error as er:
            return False, "Ocorreu um erro na busca do usuário"
