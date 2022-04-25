from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.boxlayout import BoxLayout
import kivy
import cProfile

kivy.require('1.9.1')

Window.size = (370, 600)

class MyRoot(BoxLayout):
    
    def __init__(self):
        super(MyRoot, self).__init__()

    def calc_symbol(self, symbol):
        self.calc_field.text +=symbol

    def clear(self):
        self.calc_field.text= ""

    def get_result(self):
        self.calc_field.text= str(eval(self.calc_field.text))



class MainApp(MDApp):

    def on_start(self):
        self.profile = cProfile.Profile()
        self.profile.enable()

    def on_stop(self):
        self.profile.disable()
        self.profile.dump_stats('mainapp.profile')

    def build(self):
        self.title= "KivyMD Calculator"
        return MyRoot()

mainapp= MainApp()
mainapp.run()