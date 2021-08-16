from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout


class CalcLayout(BoxLayout):
    pass


class CalculatorApp(App):
    Config.set('graphics', 'resizable', '0')
    Config.set('graphics', 'width', '275')
    Config.set('graphics', 'height', '483')


CalculatorApp().run()
