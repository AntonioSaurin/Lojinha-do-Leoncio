from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import *
from kivymd.uix.screenmanager import MDScreenManager



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

Builder.load_file("design.kv") 


class LoginScreen(MDScreen):
    
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

class MenuScreen(MDScreen):
    pass


class MainApp(MDApp):    
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"


        MDApp.title = "Lojinha do Leoncio"

        # sm.add_widget(LoginScreen(name='login'))
        global sm
        
        sm = MDScreenManager()

        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MenuScreen(name='menu'))

        return sm
        
    
if __name__ == '__main__':
    MainApp().run()