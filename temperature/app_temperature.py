from temperature.operator_temp import Change
import re

class AppTemperature(): 
    def __init__(self):
        self.f = 0
        self.t = 0
        self.entry = 0

    def apply(self, aply, result):
        self.text = aply.get()
        if re.fullmatch(r"\d*\.\d*", self.text) or re.fullmatch(r"\d+", self.text):
            if self.text == '.':
                self.entry = 0.0
            else:
                self.entry = float(self.text)
            self.operator = Change(self.f, self.t, self.entry)
            ansewr = self.operator.change()
            result.configure(text=ansewr, text_color='black')
        else:
            result.configure(text='enter valid number')

    def get_check_from(self, value):
        self.f = value

    def get_check_to(self, value):
        self.t = value
    
    