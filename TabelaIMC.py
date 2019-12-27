from openpyxl import *


class Gerar_tabela(object):
    def __init__(self, sex='', peso=0, altura=0, nome='', result='', ava=''):
        self.info = {}
        self.sex = sex
        self.peso = peso
        self.altura = altura
        self.nome = nome
        self.result = result
        self.ava = ava

    def gerar(self):
        wb = Workbook()
        try:
            wbimc = wb.active

            wbimc.merge_cells('E1:F1')

            wbimc['A1'] = 'Sexo'
            wbimc['B1'] = 'Peso'
            wbimc['C1'] = 'Altura'
            wbimc['D1'] = 'Resultado'
            wbimc['E1'] = 'Avaliação'
            wbimc['A2'] = self.sex
            wbimc['B2'] = self.peso
            wbimc['C2'] = self.altura
            wbimc['D2'] = self.result
            wbimc['E2'] = self.ava

            wb.security.workbook_password = '314159265359'
            wb.security.lockStructure = True
            wb.security.lockWindows = True
            wbimc.protection.password = '314159265359'
            return wb.save('IMC {}.xlsx'.format(self.nome))
        except:
            return ValueError('ERROR 01')
