class Change():
    def __init__(self, f, t, amount):
        self.f = f
        self.t = t
        self.amount = amount
    
    def change(self, From, To, entry):
        if From=='Celsius' and To=='Celsius':
            return entry
        elif From=='Celsius' and To=='Kelvin':
            entry += 273.15
            return entry
        elif From=='Celsius' and To=='Fahrenheit':
            entry *= 1.8
            entry += 32
            return entry
        elif From=='Kelvin' and To=='Celsius':
            entry -= 273.15
            return entry
        elif From=='Kelvin' and To=='Kelvin':
            return entry
        elif From=='Kelvin' and To=='Fahrenheit':
            res = 1.8*(entry-273.15)+32 
            return res
        elif From=='Fahrenheit' and To=='Fahrenheit':
            return entry
        elif From=='Fahrenheit' and To=='Kelvin':
            res = entry -32
            res *= 5
            res /= 9
            res += 273.15
            return res
        else:
            res = entry -32
            res *= 5
            res /= 9
            return res
        