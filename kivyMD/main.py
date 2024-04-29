from kivy.lang import Builder
from kivy.app import App
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import *
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.list import MDListItemSupportingText, MDListItem, MDListItemHeadlineText, MDListItemLeadingIcon, MDListItemTertiaryText
from kivy.modules import inspector
from kivy.core.window import Window
from kivy.properties import DictProperty


import mysql.connector


#Aqui é onde passa o endereço da instancia do banco, junto com o login e a senha + o nome da database
try:
    db = mysql.connector.connect(
        host='localhost',
        username='root',
        password='',
        database='leoncioStore'
    )
except mysql.connector.errors.ProgrammingError:
    db = mysql.connector.connect(
        host='localhost',
        username='root',
        password='',
    )
    cursor = db.cursor()
    
    cursor.execute('''
create database leoncioStore 
default char set utf8mb4 
default collate utf8mb4_general_ci;

use leoncioStore;

create table `itens`(
`id` int auto_increment,
`description` varchar(50),
`value` int,
`role` enum('Bruiser','Mage','Tank','Support','ADCarry','Assassin'),
primary key(id)
);

create table `users`(
`id` int auto_increment,
`username` varchar(20) unique,
`password` varchar(255),
`function` enum('Admin', 'Buyer'),
primary key(id)
);

insert into `users` (`username`, `password`) values ('Leoncio', 'Admin');

insert into `itens` (`description`, `value`, `role`) values('Eclipse','2800','Assassin');
insert into `itens` (`description`, `value`, `role`) values('Armadura de Warmog','3100','Tank');
insert into `itens` (`description`, `value`, `role`) values('Cutelo Negro','3000','Bruiser');
insert into `itens` (`description`, `value`, `role`) values('Força Do Vendaval','3400','ADCarry');
insert into `itens` (`description`, `value`, `role`) values('Companheiro de Luden','2900','Mage');
insert into `itens` (`description`, `value`, `role`) values('Cajado Aquafluxo','2300','Support');
                   ''')
    
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
                    role = "knife-military"


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
            
            data = (item_name, item_price, item_type)
            sql = "INSERT INTO itens (description, value, role) VALUES (%s, %s, %s)"

            cursor.execute(sql, data)
            db.commit()
        except:
            print("ERROR!!!")
        else:
            sm.current = "loja"



class RemoveScreen(MDScreen):

    global delete_item
    global edit_item


    def searching_edit(self):

        #inspector.create_inspector(Window, self.ids.container_delete)

        self.ids.container_delete_search.clear_widgets()
        data = self.delete_txt.text
        self.delete_txt.text = ''

        if data == '':
           #self.ids.tela_de_remover.add_widget()
            pass

        else:
            cursor.execute(f"SELECT * FROM itens WHERE description LIKE '%{data}%' LIMIT 1;")

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

                self.ids.container_delete_search.add_widget(
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
                        pos_hint={"center_x": .54, "center_y": .38},
                        size_hint_x=0.79,
                        divider=True,
                        id="remove_lista"
                    )
                )

                self.ids.container_delete_search.add_widget(
                    MDFabButton(
                        icon= "delete",
                        style= "standard",
                        pos_hint= {"center_x": 1.01, "center_y": .38},
                        on_press= delete_item 
                    )
                )
                self.ids.container_delete_search.add_widget(
                    MDFabButton(
                        icon= "lead-pencil",
                        style= "standard",
                        pos_hint= {"center_x": .87, "center_y": .38},
                        on_press= edit_item,
                        #on_release= self.root.searching_edit
                    )
                )

        self.delete_txt.text = ''
        #self.ids.container_delete_search.clear_widgets()

    def delete_item(self):

        #RemoveScreen.ids.container_delete_search.clear_widgets()
        try:
            sql = "DELETE FROM itens WHERE id = %s"
            where = (result[0][0], )

            cursor.execute(sql, where)
            db.commit()
            sm.current = "loja"
        except:
            print("ERROR!!")
        else:
            pass


    def edit_item(self):
        global edited_item
        edited_item = result
        # EditScreen.item_name.text = result[0][1]
        sm.current = "edit"        
        return





class EditScreen(MDScreen):
    
    def selected(self):
        print("oi")
        self.item_name.text = edited_item[0][1]
        self.item_price.text = str(edited_item[0][2])
        
    
    def selected_type(self, tipo):
        global item_type
        item_type = tipo

    def adicionar(self):
        try:
            print("Oi") 
            item_name = self.item_name.text
            item_price = self.item_price.text          
            print(item_type)
            sql = "UPDATE itens SET description = %s, value = %s, role = %s WHERE id = %s LIMIT 1"
            data = (item_name, item_price, item_type, result[0][0])

            cursor.execute(sql, data)
            db.commit()   
        except:
            print("ËRRO!!!!!!!")
        else:
            sm.current = "loja"

        

class MainApp(MDApp):    
    def move(self, tela):
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
        sm.add_widget(LojaScreen(name='loja'))
        sm.add_widget(AddScreen(name='add'))

        sm.add_widget(EditScreen(name='edit'))

        return sm
        
    
if __name__ == '__main__':
    MainApp().run()