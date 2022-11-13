from kivy.app import App
from kivy.properties import (
    ObjectProperty,StringProperty,NumericProperty
)
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout 

class LARPy(Widget):
    txt_string = ObjectProperty()
    search_input = ObjectProperty()

    def __init__(self):
        super().__init__()
        self.txt_string.text = "Press the search button to\ndisplay your text."

    def search_txt(self):
        self.txt_string.text = self.search_input.text 
        
        

class LARPyApp(App):
    def build(self):
        name=LARPy()
        return name

if __name__ == "__main__":
    LARPyApp().run()