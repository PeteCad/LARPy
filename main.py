from kivy.app import App
from kivy.properties import (
    ObjectProperty,StringProperty,NumericProperty
)
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

#Start up the Root window and set initial screen
#We'll change this based on user permissions later
class LARPyRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu="Admin"
        self.show_menu()
        
    def show_menu(self):
        cur_menu=AdminPanel()
        # self.add_widget(cur_menu)

# This menu is the initial admin layout. This is going to be fix with
# choices of user mofification(Add, remove, reset), create/remove game, 
# backup, at this time the whole backend hasn't been created
class AdminPanel(BoxLayout):
    pass

class LARPyApp(App):
    def build(self):
        larpy_main=LARPyRoot()
        return larpy_main

if __name__ == "__main__":
    LARPyApp().run()