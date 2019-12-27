from IMCal.BDIMC import Banco


class User(object):
    def __init__(self, nome='', sex='', peso=0, altura=0, result='', ava=''):
        self.info = {}
        self.nome = nome
        self.sex = sex
        self.peso = peso
        self.altura = altura
        self.result = result
        self.ava = ava

    def inserir_dados(self):
        banco = Banco()
        try:
            c = banco.conn.cursor()
            c.execute("INSERT INTO imc (Nome, Sexo, Peso, Altura, Resultado, Avaliação) VALUES (?, ?, ?, ?, ?, ?)",
                      (self.nome, self.sex, self.peso, self.altura, self.result, self.ava))

            banco.conn.commit()

            return 'okay'
        except:
            return 'ERROR'
