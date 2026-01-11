class Change():
    def __init__(self, f, t, amount):
        self.From = f
        self.To = t
        self.entry = amount
    
    def change(self):
        if self.From=='Celsius' and self.To=='Celsius':
            return self.entry
        elif self.From=='Celsius' and self.To=='Kelvin':
            self.entry += 273.15
            return self.entry
        elif self.From=='Celsius' and self.To=='Fahrenheit':
            self.entry *= 1.8
            self.entry += 32
            return self.entry
        elif self.From=='Kelvin' and self.To=='Celsius':
            self.entry -= 273.15
            return self.entry
        elif self.From=='Kelvin' and self.To=='Kelvin':
            return self.entry
        elif self.From=='Kelvin' and self.To=='Fahrenheit':
            self.res = 1.8*(self.entry-273.15)+32 
            return self.res
        elif self.From=='Fahrenheit' and self.To=='Fahrenheit':
            return self.entry
        elif self.From=='Fahrenheit' and self.To=='Kelvin':
            self.res = self.entry -32
            self.res *= 5
            self.res /= 9
            self.res += 273.15
            return self.res
        elif self.From=='Fahrenheit' and self.To=='Celsius':
            self.res = self.entry -32
            self.res *= 5
            self.res /= 9
            return self.res
        else:
            return "please fill the box"