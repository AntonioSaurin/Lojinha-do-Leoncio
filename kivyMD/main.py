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
    item_price = ObjectProperty(None)
    item_name = ObjectProperty(None)
    delete_txt = ObjectProperty(None)

    def press(self):
        #Aqui é atribuido valor as variaveis
        user = (self.user.text,)
        password = self.password.text

        cursor.execute("SELECT * FROM `users` WHERE `username`=%s",user)

        result = cursor.fetchall()

        if result:
            print(result)
            if password == result[0][2]:
                self.password.text = ''
                sm.current = "loja"
            else:
                print("Senha incorreta")
        else:
            print("nenhum registro")

class LojaScreen(MDScreen):
    def searching(self):
        data = self.search.text
        self.ids.container.clear_widgets()

        if data == '':
            cursor.execute("SELECT * FROM itens")
            result = cursor.fetchall()
            for x in result:
                if x[3] == "Tank":
                    role = "shield"
                elif x[3] == "Bruiser":
                    role = "sword"
                elif x[3] == "Mage":
                    role = "star-four-points"
                elif x[3] == "Support":
                    role = "medication"
                elif x[3] == "ADCarry":
                    role = "bow-arrow"
                elif x[3] == "Assassin":
                    role = "knige-military"

                print(x)

                self.ids.container.add_widget(
                    MDListItem(
                        MDListItemLeadingIcon(
                            icon=role,
                        ),
                        MDListItemHeadlineText(
                            text=f"{x[1]}",
                        ),
                        MDListItemSupportingText(
                            text=f"{x[2]}g",
                        ),    
                        MDListItemTertiaryText(
                            text=f"{x[3]}",
                            padding= [0, 10, 0, 0],
                        ),
                        
                        pos_hint={"center_x": .5, "center_y": .5},
                        size_hint_x=0.8,
                        divider=True,
                    ) 
                )
        else:
            cursor.execute(f"SELECT * FROM itens WHERE description LIKE '%{data}%'")
            result = cursor.fetchall()

            for x in result:
                if x[3] == "Tank":
                    role = "shield"
                elif x[3] == "Bruiser":
                    role = "sword"
                elif x[3] == "Mage":
                    role = "magic-staff"
                elif x[3] == "Support":
                    role = "medication"
                elif x[3] == "ADCarry":
                    role = "bow-arrow"
                elif x[3] == "Assassin":
                    role = "knife-military"

                print(x)

                self.ids.container.add_widget(
                    MDListItem(
                        MDListItemLeadingIcon(
                            icon=role,
                        ),
                        MDListItemHeadlineText(
                            text=f"{x[1]}",
                        ),
                        MDListItemSupportingText(
                            text=f"{x[2]}g",
                        ),    
                        MDListItemTertiaryText(
                            text=f"{x[3]}",
                            padding= [0, 10, 0, 0],
                        ),
                        
                        pos_hint={"center_x": .5, "center_y": .5},
                        size_hint_x=0.8,
                        divider=True,
                    ) 
                )


class AddScreen(MDScreen):

    def selected_type(self, tipo):
        global item_type
        item_type = tipo


    def adicionar(self):
        try:
            item_name = self.item_name.text
            item_price = self.item_price.text          
            print(item_type)

            print(f"Nome: {item_name}, preço {item_price}, tipo: {item_type}")
        except:
            print("ËRRO!!!!!!!")
        else:
            pass



class RemoveScreen(MDScreen):

    global delete_item
    global edit_item

    def searching(self):
        data = self.delete_txt.text
        try:
            self.ids.container_delete.remove_widget(MDListItem)
        except:
            print("ERRO")
        else:
            pass

        if data == '':
           #self.ids.tela_de_remover.add_widget()
            pass

        else:
            cursor.execute(f"SELECT * FROM itens WHERE description LIKE '%{data}%' LIMIT 1;")
            
            global edited_item


            global result
            result = cursor.fetchall()

            for x in result:
                if x[3] == "Tank":
                    role = "shield"
                elif x[3] == "Bruiser":
                    role = "sword"
                elif x[3] == "Mage":
                    role = "magic-staff"
                elif x[3] == "Support":
                    role = "medication"
                elif x[3] == "ADCarry":
                    role = "bow-arrow"
                elif x[3] == "Assassin":
                    role = "knife-military"

                self.ids.container_delete.add_widget(
                    MDListItem(
                        MDListItemLeadingIcon(
                            icon=role,
                        ),
                        MDListItemHeadlineText(
                            text=f"{x[1]}",
                        ),
                        MDListItemSupportingText(
                            text=f"{x[2]}g",
                        ),    
                        MDListItemTertiaryText(
                            text=f"{x[3]}",
                            padding= [0, 0, 0, 0],
                        ),
                        pos_hint={"center_x": .43, "center_y": .38},
                        size_hint_x=0.79,
                        divider=True,

                    )
                )

                def delete_item(self):
                    print(result)

                self.ids.container_delete.add_widget(
                    MDFabButton(
                        icon= "delete",
                        style= "standard",
                        pos_hint= {"center_x": .90, "center_y": .38},
                        on_press= delete_item
                    )
                )
                self.ids.container_delete.add_widget(
                    MDFabButton(
                        icon= "lead-pencil",
                        style= "standard",
                        pos_hint= {"center_x": .77, "center_y": .38},
                        on_press= edit_item
                    )
                )
    global edit_item
    def edit_item(self):
        global edited_item
        edited_item = result
        print(result)
        print(edited_item[0][1])
        sm.current = "edit"
        return(edited_item[0][1])




class EditScreen(MDScreen):
    
    def selected_type(self, tipo):
        global item_type
        item_type = tipo

    def adicionar(self):
        try:
            item_name = self.item_name.text
            item_price = self.item_price.text          
            print(item_type)

            print(f"Nome: {item_name}, preço {item_price}, tipo: {item_type}")
        except:
            print("ËRRO!!!!!!!")
        else:
            pass

        

class MainApp(MDApp):    
    def move(self, tela):
        print(tela)
        if tela == "login":
            sm.current = "login"
        elif tela == "add":
            sm.current = "add"
        elif tela == "loja":
            sm.current = "loja"
        elif tela == "remove":
            sm.current = "remove"
        elif tela == "edit":
            sm.current = "edit"
        else:
            pass
    



    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"


        MDApp.title = "Lojinha do Leoncio"

        # sm.add_widget(LoginScreen(name='login'))
        global sm
        
        sm = MDScreenManager()

        sm.add_widget(RemoveScreen(name='remove'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(EditScreen(name='edit'))
        sm.add_widget(LojaScreen(name='loja'))
        sm.add_widget(AddScreen(name='add'))

        return sm
        
    
if __name__ == '__main__':
    MainApp().run()