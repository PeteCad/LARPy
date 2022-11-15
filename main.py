# External imports
from kivy.app import App
from kivy.properties import (
    ObjectProperty,StringProperty,NumericProperty
)
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
# Project imports
from db_func import *

#Start up the Root window and set initial screen
#We'll change this based on user permissions later
class LARPyRoot(Widget):
    menu_list={}
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.show_menu(menu="admin")     #create splash screen(will be login later)
        
    def show_menu(self, **kwargs):
        
        #This code should be moved to more appropriate places as they are
        #created. It's likely we'll have multiple character "tabs" for example
        #or possibly multiple "game" tabs with multiple user
        if "menu" in kwargs:
            if kwargs["menu"] == "admin":
                if not "admin" in self.menu_list:
                    cur_menu=AdminPanel()
                    self.menu_list.update({"admin" : cur_menu})
                else:
                    cur_menu=self.menu_list["admin"]
            elif kwargs["menu"] == "user":
                if not "user" in self.menu_list:
                    cur_menu=UserPanel()
                    self.menu_list.update({"user":cur_menu})
                else:
                    cur_menu=self.menu_list["user"]
            elif kwargs["menu"] == "character":
                if not "character" in self.menu_list:
                    cur_menu=CharacterPanel()
                    self.menu_list.update({"character":cur_menu})
                else:
                    cur_menu=self.menu_list["character"]
                    
            self.add_widget(cur_menu)
        
        
# This menu is the initial admin layout. This is going to be fix with
# choices of user mofification(Add, remove, reset), create/remove game, 
# backup, at this time the whole backend hasn't been created
class AdminPanel(BoxLayout):
    def game_create(self):
        game_create()

class LARPyApp(App):
    def build(self):
        larpy_main=LARPyRoot()
        return larpy_main
    def quit(self):
        quit()

if __name__ == "__main__":
    LARPyApp().run()
    
