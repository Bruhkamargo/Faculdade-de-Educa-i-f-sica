import wx
from IMCal import TabelaIMC, GeradorRelatorio, ENTRYIMC


class Window(wx.Frame):

	def __init__(self, *args, **kw):
		super(Window, self).__init__(*args, **kw)
		self.menu_superior()

		panel = wx.Panel(self, pos=(20, 20))
		text1 = wx.StaticText(panel, -1, 'Calculadora IMC', (60, 10))
		ft1 = text1.GetFont()
		ft1.PointSize += 10
		ft1 = ft1.Bold()
		text1.SetFont(ft1)
		text2 = wx.StaticText(panel, -1, 'Nome:', (40, 90))
		text3 = wx.StaticText(panel, -1, 'Peso:', (40, 130))
		text4 = wx.StaticText(panel, -1, 'Altura:', (40, 180))
		text5 = wx.StaticText(panel, -1, 'Resultados', (60, 280))
		ft2 = text5.GetFont()
		ft2.PointSize += 8
		ft2 = ft2.Bold()
		text5.SetFont(ft2)
		text6 = wx.StaticText(panel, -1, 'IMC: ', (40, 320))
		ft3 = text6.GetFont()
		ft3.PointSize += 2
		ft3 = ft3.Bold()
		text6.SetFont(ft3)
		text7 = wx.StaticText(panel, -1, 'IMC: ', (40, 360))
		ft4 = text7.GetFont()
		ft4.PointSize += 2
		ft4 = ft4.Bold()
		text7.SetFont(ft4)
		self.text8 = wx.StaticText(panel, -1, '', (80, 324))
		self.text9 = wx.StaticText(panel, -1, '', (80, 364))
		self.box1 = wx.TextCtrl(panel, -1, pos=(90, 90))
		self.box2 = wx.TextCtrl(panel, -1, pos=(90, 130))
		self.box3 = wx.TextCtrl(panel, -1, pos=(90, 180))
		self.rb1 = wx.RadioButton(panel, -1, 'Maculino', (90, 60), style=wx.RB_GROUP)
		self.rb2 = wx.RadioButton(panel, -1, 'Feminino', (180, 60))
		bmp_h = wx.Bitmap('help_icon.png')
		bth = wx.BitmapButton(panel, -1, bitmap=bmp_h, size=(bmp_h.GetWidth(), bmp_h.GetHeight()), pos=(350, 0))
		bt1 = wx.Button(panel, -1, 'Calcular IMC', (40, 220))
		bt2 = wx.Button(panel, -1, 'Novo IMC', (160, 220))
		bt3 = wx.Button(panel, -1, 'Reletorio', (280, 220))

		self.Bind(wx.EVT_BUTTON, self.bt1_click, bt1)
		self.Bind(wx.EVT_BUTTON, self.bt2_click, bt2)
		self.Bind(wx.EVT_BUTTON, self.bt3_click, bt3)
		self.Bind(wx.EVT_BUTTON, self.bt_about, bth)
		self.Bind(wx.EVT_RADIOBUTTON, None, self.rb1)
		self.Bind(wx.EVT_RADIOBUTTON, None, self.rb2)

		self.status_bar()

	def menu_superior(self):
		file_menu = wx.Menu()
		iten11 = file_menu.Append(-1, "Olá\tCtrl+1", "Olá Mundo")
		file_menu.AppendSeparator()
		iten12 = file_menu.Append(wx.ID_EXIT)

		help_menu = wx.Menu()
		item21 = help_menu.Append(wx.ID_ABOUT, "Sobre\tCtrl+3", 'Sobre')

		edit_menu = wx.Menu()
		item31 = edit_menu.Append(wx.ID_UNDO, "Desfazer\tCtrl+z")
		item32 = edit_menu.Append(-1, "Refazer")

		menu_bar = wx.MenuBar()
		menu_bar.Append(file_menu, "Arquivo")
		menu_bar.Append(edit_menu, "Editar")
		menu_bar.Append(help_menu, "Ajuda")
		self.SetMenuBar(menu_bar)
		self.Bind(wx.EVT_MENU, self.bt_hello, iten11)
		self.Bind(wx.EVT_MENU, self.bt_exit, iten12)
		self.Bind(wx.EVT_MENU, self.bt_about, item21)
		self.Bind(wx.EVT_MENU, None, item31)
		self.Bind(wx.EVT_MENU, None, item32)

	def status_bar(self):
		self.CreateStatusBar()
		self.SetStatusText("	Desenvolvido por: LAB-BCS© === @Bruhkamargo")

	def bt_exit(self, event):
		self.Close(True)

	def bt_hello(self, event):
		wx.MessageBox("Olá, Usuario", "Olá")

	def bt_about(self, event):
		wx.MessageBox("Calculadora de IMC desenvolvida\n"
					  "como teste para a aquisição de dados\n"
					  "e tratamentos por meio de banco de dados.\n\n\n @labbcs", "Sobre",
					  wx.OK | wx.ICON_INFORMATION)

	def bt1_click(self, event):
		print(self.bt1_click)
		tab = TabelaIMC.Gerar_tabela()
		user = ENTRYIMC.User()
		var1 = self.rb1.GetValue()
		var2 = self.rb2.GetValue()
		nome = str(self.box1.GetValue())
		p = int(self.box2.GetValue())
		h = int(self.box3.GetValue())
		tab.nome = nome
		tab.peso = p
		tab.altura = h
		user.nome = nome
		user.peso = p
		user.altura = h
		result = float(p) / ((float(h) / 100) ** 2)
		tab.result = ("{:.2f}".format(result))
		user.result = str(result)
		self.text8.SetLabel('{:.2f} Pontos'.format(result))
		if var1 == True:
			tab.sex = 'Masc.'
			user.sex = 'Masc.'
			if result < 20.69:
				self.text9.SetLabel("IMC Abaixo do Normal")
			elif result <= 26.40:
				self.text9.SetLabel("IMC Normal")
			elif result <= 27.80:
				self.text9.SetLabel("IMC Acima do Peso")
			elif result <= 32.30:
				self.text9.SetLabel("IMC Obesidade")
			else:
				self.text9.SetLabel("IMC Obesidade Morbida")
		if var2 == True:
			tab.sex = 'Fem.'
			user.sex = 'Fem.'
			if result < 19.09:
				self.text9.SetLabel("IMC Abaixo do Normal")
			elif result <= 25.80:
				self.text9.SetLabel("IMC Normal")
			elif result <= 27.30:
				self.text9.SetLabel("IMC Acima do Peso")
			elif result <= 32.30:
				self.text9.SetLabel("IMC Obesidade ")
			else:
				self.text9.SetLabel("IMC Obesidade Morbida")
		result2 = self.text9.GetLabel()
		tab.ava = result2
		user.ava = ('{}'.format(result2))
		print(tab.gerar())
		print(user.inserir_dados())

	def bt2_click(self, event):
		print(self.bt2_click)
		self.rb1.SetValue(0)
		self.rb2.SetValue(0)
		self.box1.SetValue('')
		self.box2.SetValue('')
		self.box3.SetValue('')
		self.text8.SetLabel('')
		self.text9.SetLabel('')

	def bt3_click(self, event):
		print(self.bt3_click)
		GeradorRelatorio.read_data()


if __name__ == '__main__':
	app = wx.App()
	frm = Window(None, title='Calculadora IMC')
	frm.SetBackgroundColour('white')
	frm.Show()
	app.MainLoop()
