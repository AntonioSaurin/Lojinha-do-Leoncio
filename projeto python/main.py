from kivy.lang import Builder
from kivymd.app import MDApp as App
# from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import *

import mysql.connector

#Aqui é onde passa o endereço da instancia do banco, junto com o login e a senha + o nome da database
db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='leoncioStore'
)

#Esse é o cursor que vai execurar os comandos no bancopy 
cursor = db.cursor()

#Aqui é definido a conexao do documento do kivy, tipo linkar o css
Builder.load_file('design.kv')
        
sm = ScreenManager()

#aqui entra toda a logica e conteudo referente a pagina de Login, o nome da classe determina que elementos do documento .kv serao inseridos aqui
class LoginScreen(Screen):
    
    
    #Aqui é definido as variaveis dos inputs do design.kv
    user = ObjectProperty(None)
    password = ObjectProperty(None)

    def press(self):

        #Aqui é atribuido valor as variaveis
        user = (self.user.text,)
        password = self.password.text

        cursor.execute("SELECT * FROM `users` WHERE `username`=%s",user)

        result = cursor.fetchall()

        if result:
            print(result)
            if password == result[0][2]:
                sm.current = "menu"
            else:
                print("Senha incorreta")
        else:
            print("nenhum registro")
        
        #E caso as credencias do leoncio estejam corretas ele prossege para o menu
        # if user == "Leoncio" and password == "123":
        #     sm.current = "menu"

    def show_password(self):
        if self.ids.password.password is False:
            self.ids.password_buttom.icon = 'eye-off'
            self.ids.password.password = True
        else:
            self.ids.password_buttom.icon = 'eye'
            self.ids.password.password = False

#Mesma coisa do login porem n fiz logica nenhuma nessa pagina kk
class MenuScreen(Screen):
    pass

class MyApp(App):
    def build(self):

        #Define o titulo do App
        App.title = "Lojinha do Leoncio"

        #aqui é criado o gerenciador de telas e nele sao inseridas as duas paginas
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MenuScreen(name='menu'))
        
        return sm
    
#Coloca o programa pra rodar
if __name__ == '__main__':
    MyApp().run()