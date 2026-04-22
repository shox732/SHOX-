from kivy.app import App
from kivy.uix.label import Label

class ShoxGram(App):
    def build(self):
        return Label(text='Salom! Bu Shox Gram ilovasi!')

if __name__ == '__main__':
    ShoxGram().run()
