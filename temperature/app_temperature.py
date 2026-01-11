from temperature.operator_temp import Change

class AppTemperature():
    def __init__(self):
        self.f = 0
        self.t = 0
        self.entry = 0
        self.operator = Change(self.f, self.t, self.entry)

    def apply(self, aply, result):
        self.entry = float(aply.get())
        ansewr = self.operator.change(self.f, self.t, self.entry)
        result.configure(text=ansewr, text_color='black')

    def get_check_from(self, value):
        self.f = value

    def get_check_to(self, value):
        self.t = value
    
    