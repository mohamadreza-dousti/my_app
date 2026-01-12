import math

class Operate():
    def __init__(self):
        pass
    def add(self, lst):
        self.ansewr = 0
        for i in lst:
            self.ansewr += i
        return self.ansewr
    
    def sub(self, lst):
        self.ansewr = lst[0]
        for i in lst[1:]:
            self.ansewr -= i
        return self.ansewr
    
    def div(self, lst):
        self.ansewr = lst[0]
        for i in lst[1:]:
            if i != 0:
                self.ansewr /= i
            else:
                self.ansewr = 0
        return self.ansewr
    
    def mul(self, lst):
        self.ansewr = lst[0]
        for i in lst[1:]:
            self.ansewr *= i
        return self.ansewr
    
    def rad(self, lst):
        self.ansewr = math.sqrt(lst[0])
        return self.ansewr
    
    def my_pow(self, lst):
        self.ansewr = math.pow(lst[0], 2)
        return self.ansewr
    
    def ded(self, lst):
        self.ansewr = lst[0]
        if self.ansewr != 0:
            self.ansewr = 1/lst[0]
        else:
            self.ansewr = 0
        return self.ansewr
    
    def cor(self, lst):
        self.ansewr = -lst[0]
        return self.ansewr