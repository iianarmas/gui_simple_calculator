from kivy.app import App
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class CalcLayout(BoxLayout):
    screen_text = StringProperty('')
    new_value = StringProperty('0')

    def on_button_1_click(self):
        self.screen_text += '1'

    def on_button_2_click(self):
        self.screen_text += '2'

    def on_button_3_click(self):
        self.screen_text += '3'

    def on_button_4_click(self):
        self.screen_text += '4'

    def on_button_5_click(self):
        self.screen_text += '5'

    def on_button_6_click(self):
        self.screen_text += '6'

    def on_button_7_click(self):
        self.screen_text += '7'

    def on_button_8_click(self):
        self.screen_text += '8'

    def on_button_9_click(self):
        self.screen_text += '9'

    def on_button_0_click(self):
        self.screen_text += '0'

    def on_button_pt_click(self):
        self.screen_text += '.'

    def on_button_add_click(self):
        self.screen_text += ' + '

    def on_button_sub_click(self):
        self.screen_text += ' - '

    def on_button_mul_click(self):
        self.screen_text += ' * '

    def on_button_div_click(self):
        self.screen_text += ' / '

    def on_button_can_click(self):
        self.screen_text = str('')
        self.new_value = str('0')

    def on_button_eql_click(self):
        self.calculate()
        self.screen_text = self.new_value

    def calculate(self):
        num_list = [i for i in self.screen_text.split()]

        if len(num_list) >= 3:
            num_list_check = [i for i in num_list if i.isdigit() or i.isdecimal()]
            if len(num_list_check) == 1:
                self.new_value = num_list_check[0]
            elif len(num_list_check) == 0:
                self.new_value = '0'
            else:
                if num_list[1] == '+':
                    temp_value = str(float(num_list[0]) + float(num_list[2]))
                    if temp_value == '0.0':
                        self.new_value = '0'
                    else:
                        self.new_value = temp_value.strip('0.0')
                elif num_list[1] == '-':
                    temp_value = str(float(num_list[0]) - float(num_list[2]))
                    if temp_value == '0.0':
                        self.new_value = '0'
                    else:
                        self.new_value = temp_value.strip('0.0')
                elif num_list[1] == '*':
                    temp_value = str(float(num_list[0]) * float(num_list[2]))
                    if temp_value == '0.0':
                        self.new_value = '0'
                    else:
                        self.new_value = temp_value.strip('0.0')
                elif num_list[1] == '/':
                    if num_list[2] == '0':
                        self.new_value = "INF"
                    else:
                        temp_value = str(float(num_list[0]) / float(num_list[2]))
                        if temp_value == '0.0':
                            self.new_value = '0'
                        else:
                            self.new_value = temp_value.strip('0.0')
        elif len(num_list) < 3:
            num_list_check = [i for i in num_list if i.isdigit()]
            if len(num_list_check) == 1:
                self.new_value = num_list_check[0]
            else:
                self.new_value = '0'


class CalculatorApp(App):
    '''Config.set('graphics', 'resizable', '0')
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '780')'''

    def build(self):
        return CalcLayout()


if __name__ == "__main__":
    CalculatorApp().run()
