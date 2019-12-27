import sqlite3


path = r"C:\Users\User\PycharmProjects\bioestatistica\IMCal\DataBase"


class Banco:

    def __init__(self):
        self.conn = sqlite3.connect(path+r'\imc.db')
        self.gerar_tabela()

    def gerar_tabela(self):
        c = self.conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS imc (Nome text, Sexo text, '
                  'Peso integer, Altura integer, Resultado text, Avaliação text)')

        c.close()
