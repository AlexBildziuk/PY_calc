from kivy.app import App
import math

from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config

window_height = 480
window_width = 320

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', window_width)
Config.set('graphics', 'height', window_height)

class CalculatorApp(App):
    
    def build(self):
        self.formula = "0"
        self.number = 0
        self.operator = ""
        gl_spacing = 1
        bl_padding = 3
        lbl_height = .25
        bl = BoxLayout(orientation = 'vertical', padding = bl_padding)
        gl = GridLayout(cols = 4, spacing = gl_spacing, size_hint = (1, 1 - lbl_height))

        self.lbl = Label(text="0", font_size = 40, valign = "center", halign = "right", size_hint = (1, lbl_height), text_size=(window_width - 2*bl_padding, window_height*lbl_height - 2*bl_padding))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='x\u00B2', on_press = self.degree2))
        gl.add_widget(Button(text= '\u221A', on_press = self.root2))
        gl.add_widget(Button(text="1/x", on_press = self.reverse))
        gl.add_widget(Button(text="<=", on_press = self.clear_one))

        gl.add_widget(Button(text="+/-", on_press = self.invert))
        gl.add_widget(Button(text="%", on_press = self.operator_proc))
        gl.add_widget(Button(text="!", on_press = self.fact))
        gl.add_widget(Button(text="AC", on_press = self.clear_AC))
        
        gl.add_widget(Button(text="7", on_press = self.add_number))
        gl.add_widget(Button(text="8", on_press = self.add_number))
        gl.add_widget(Button(text="9", on_press = self.add_number))
        gl.add_widget(Button(text="/", on_press = self.operator_dev))

        gl.add_widget(Button(text="4", on_press = self.add_number))
        gl.add_widget(Button(text="5", on_press = self.add_number))
        gl.add_widget(Button(text="6", on_press = self.add_number))
        gl.add_widget(Button(text="x", on_press = self.operator_mult))

        gl.add_widget(Button(text="1", on_press = self.add_number))
        gl.add_widget(Button(text="2", on_press = self.add_number))
        gl.add_widget(Button(text="3", on_press = self.add_number))
        gl.add_widget(Button(text="-", on_press = self.operator_minus))

        gl.add_widget(Button(text="0", on_press = self.add_number))
        gl.add_widget(Button(text=".", on_press = self.add_dot))
        gl.add_widget(Button(text="=", on_press = self.operator_eq))
        gl.add_widget(Button(text="+", on_press = self.operator_plus))

        bl.add_widget(gl)
        
        return bl

    def clear_AC(self, instance):
        self.formula = "0"
        self.number = 0
        self.operator = ""
        self.update_label()

    def invert(self, instance):
        self.formula = str((-1) * self.set_number())
        self.update_label()

    def clear_one(self, instance):
        if (len(self.formula) == 1):
            self.formula = "0"
            self.update_label()
        elif (self.formula != "0"):
            len_str = len(self.formula)
            self.formula = self.formula[0:len_str-1]
            self.update_label()

    def reverse(self, instance):
        if (self.formula == "0"):
            self.formula ="0"
        else:
            self.formula = str(1/self.set_number())
        self.treatment()
        self.update_label()
        self.formula = ""
        self.number = 0
    
    def degree2(self, instance):
        self.number = 0
        self.operator = ""
        n = self.set_number()
        self.formula = str(n*n)
        self.treatment()
        self.update_label()
        self.formula = ""

    def root2(self, instance):
        print("inside")
        self.number = 0
        self.operator = ""
        n = self.set_number()
        print(n)
        if (n < 0):
            self.formula = "0"
        else:
            self.formula = str(math.sqrt(n))
            self.treatment()
        self.update_label()
        self.formula = ""    

    def fact(self, instance):
        if (self.lbl.text == "0"):
            self.formula ="1"
        elif (self.lbl.text.find('.') != -1):
            self.formula ="0"
        else:
            n = int(self.lbl.text)
            k = 1
            for i in range(n):
                k *= (i+1)
            self.formula = str(k)
        self.update_label()
        self.formula =""

    def add_number(self, instance):
        if (self.formula == "0"):
            self.formula =""
        self.formula += str(instance.text)
        self.update_label()

    def add_dot(self, instance):
        self.formula += str(instance.text)
        self.update_label()

    def update_label(self):
        self.lbl.text = self.formula

    def operator_plus(self, instance):
        self.formula = ""
        self.number = self.set_number()
        self.operator = "plus"

    def operator_minus(self, instance):
        self.formula = ""
        self.number = self.set_number()
        self.operator = "minus"

    def operator_mult(self, instance):
        self.formula = ""
        self.number = self.set_number()
        self.operator = "mult"

    def operator_dev(self, instance):
        self.formula = ""
        self.number = self.set_number()
        self.operator = "dev"

    def operator_proc(self, instance):
        self.formula = ""
        self.number = self.set_number()
        self.operator = "proc"

    def operator_eq(self,instance):
        self.formula = self.math_operator()      
        self.treatment()
        self.update_label()
        self.operator = ""
        self.number = 0
        self.formula = ""

    def math_operator(self):
        text_return = ""
        if(self.operator == "plus"):
            text_return = str(self.set_number() + self.number)
        elif(self.operator == "minus"):
            text_return = str(self.number - self.set_number())
        elif(self.operator == "mult"):
            text_return = str(self.number * self.set_number())
        elif(self.operator == "dev"):
            if (self.set_number() != 0):
                text_return = str(self.number / self.set_number())
            else:
                 text_return = "0" 
        elif(self.operator == "proc"):
            text_return = str(self.number * self.set_number() / 100)      
        return text_return
        
    def treatment(self):
        n = self.formula.find('.0')
        k = self.formula.find('.')
        len_str = len(self.formula)
        if ((n != -1) & (n+2 == len_str)):
            self.formula = self.formula[0:len_str-2]
        elif ((k != -1) & (len_str - k > 10)):
            self.formula = self.formula[0:k+11]

    def set_number(self):
        if (self.lbl.text.find('.') != -1):
            return float(self.lbl.text)
        else:
            return int(self.lbl.text)

if __name__ == "__main__":
    CalculatorApp().run()
