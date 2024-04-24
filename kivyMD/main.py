from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import *
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.list import MDListItemSupportingText, MDListItem, MDListItemHeadlineText, MDListItemLeadingIcon, MDListItemTertiaryText


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
    search = ObjectProperty(None)


    def press(self):

        #Aqui é atribuido valor as variaveis
        user = (self.user.text,)
        password = self.password.text

        cursor.execute("SELECT * FROM `users` WHERE `username`=%s",user)

        result = cursor.fetchall()

        if result:
            print(result)
            if password == result[0][2]:
                sm.current = "loja"
            else:
                print("Senha incorreta")
        else:
            print("nenhum registro")

class LojaScreen(MDScreen):
    def on_enter(self):
        for x in range(25):
            self.ids.container.add_widget(
                MDListItem(
                    MDListItemLeadingIcon(
                        icon="shopping",
                    ),
                    MDListItemHeadlineText(
                        text=f"Item {x}",
                    ),
                    MDListItemSupportingText(
                        text=f"{x * 100}g",
                    ),    
                    MDListItemTertiaryText(
                        text="Descricao mt foda do item de numero {x}",
                        padding= [0, 10, 0, 0],
                    ),
                    
                    pos_hint={"center_x": .5, "center_y": .5},
                    size_hint_x=0.8,
                    divider=True,
                ) 
            )
               


class MainApp(MDApp):    
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"


        MDApp.title = "Lojinha do Leoncio"

        # sm.add_widget(LoginScreen(name='login'))
        global sm
        
        sm = MDScreenManager()

        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(LojaScreen(name='loja'))

        return sm
        
    
if __name__ == '__main__':
    MainApp().run()