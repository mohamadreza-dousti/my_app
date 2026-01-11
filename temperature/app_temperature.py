from temperature.operator_temp import Change

class AppTemperature():
    def __init__(self):
        self.f = 0
        self.t = 0
        self.entry = 0

    def apply(self, aply, result):
        if not aply.get() == '':
            self.entry = float(aply.get())
        self.operator = Change(self.f, self.t, self.entry)
        ansewr = self.operator.change()
        result.configure(text=ansewr, text_color='black')

    def get_check_from(self, value):
        self.f = value

    def get_check_to(self, value):
        self.t = value
    
    