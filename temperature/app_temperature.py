from temperature.operator_temp import Change

class AppTemperature():
    f = 0
    t = 0
    entry = 0
    def __init__(self):
        self.operator = Change(AppTemperature.f, AppTemperature.t, AppTemperature.entry)

    def apply(self, aply, result):
        entry = float(aply.get())
        ansewr = self.operator.change(AppTemperature.f, AppTemperature.t, entry)
        result.configure(text=ansewr, text_color='black')

    @classmethod
    def get_check_from(cls, value):
        cls.f = value

    @classmethod
    def get_check_to(cls, value):
        cls.t = value  
    
    