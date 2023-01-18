from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
import webbrowser
import dimensionamento


sm = ScreenManager()
resultado = str('.....')


class RegisterScreen(Screen):
    pass

class PrincipalScreen(Screen):
    pass

class DimensionamentoScreen(Screen):
    pass

class RiscosScreen(Screen):
    pass

class QuimicosScreen(Screen):
    a = open('matérias/quimicos.txt')
    string= str(a.read())

class FisicosScreen(Screen):
    a = open('matérias/fisicos.txt')
    string= str(a.read())

class BiologicosScreen(Screen):
    a = open('matérias/biologicos.txt')
    string= str(a.read())

class ErgonomicosScreen(Screen):
    a = open('matérias/ergonomicos.txt')
    string= str(a.read())

class AcidentesScreen(Screen):
    a = open('matérias/acidentes.txt')
    string= str(a.read())


class SesmtScreen(Screen): 
    def mudar(self):       
        try:
            g = int(self.ids.g.text)
            n = int(self.ids.t.text)
            dimensionamento.dimensionamento_sesmt(g,n)
            self.ids.error.text = ' '
            self.ids.l.text = dimensionamento.resposta 
        except:
            self.ids.error.text = 'Digite o numero correto!'
        

        
sm.add_widget(SesmtScreen(name='cipa'))
sm.add_widget(RegisterScreen(name='register'))
sm.add_widget(PrincipalScreen(name= 'principal'))
sm.add_widget(DimensionamentoScreen(name='dimensionamento'))


class TestApp(MDApp):
    def build(self):        
        kv = Builder.load_file("telas.kv")
        sm = kv
        return sm

    def open_nrs(self):
        url = 'https://www.gov.br/trabalho-e-previdencia/pt-br/composicao/orgaos-especificos/secretaria-de-trabalho/inspecao/seguranca-e-saude-no-trabalho/ctpp-nrs/normas-regulamentadoras-nrs'
        webbrowser.open(url)

TestApp().run()