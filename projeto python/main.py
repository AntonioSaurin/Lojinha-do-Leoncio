from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

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
        user = self.user.text
        password = self.password.text

        #E caso as credencias do leoncio estejam corretas ele prossege para o menu
        if user == "Leoncio" and password == "123":
            sm.current = "menu"


#Mesma coisa do login porem n fiz logica nenhuma nessa pagina kk
class MenuScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        
        #aqui é criado o gerenciador de telas e nele sao inseridas as duas paginas
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MenuScreen(name='menu'))
        
        return sm
    
#Coloca o programa pra rodar
if __name__ == '__main__':
    MyApp().run()