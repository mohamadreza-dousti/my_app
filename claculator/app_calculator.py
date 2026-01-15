from claculator.operations import Operate
import re

class AppCalculator():
    def __init__(self):
        self.numbers = []
        self.operator = 0
        self.do = Get()

    def btn_number(self, entry, button):
        self.text = entry.cget('text')
        self.text_btn = button.cget('text')
        if self.text_btn == '0':
            entry.configure(text = f'{self.text}' + '0', text_color='black')
        elif self.text_btn == '1':
            entry.configure(text = f'{self.text}' + '1', text_color='black')
        elif self.text_btn == '2':
            entry.configure(text = f'{self.text}' + '2', text_color='black')
        elif self.text_btn == '3':
            entry.configure(text = f'{self.text}' + '3', text_color='black')
        elif self.text_btn == '4':
            entry.configure(text = f'{self.text}' + '4', text_color='black')
        elif self.text_btn == '5':
            entry.configure(text = f'{self.text}' + '5', text_color='black')
        elif self.text_btn == '6':
            entry.configure(text = f'{self.text}' + '6', text_color='black')
        elif self.text_btn == '7':
            entry.configure(text = f'{self.text}' + '7', text_color='black')
        elif self.text_btn == '8':
            entry.configure(text = f'{self.text}' + '8', text_color='black')
        elif self.text_btn == '9':
            entry.configure(text = f'{self.text}' + '9', text_color='black')
        else:
            entry.configure(text = f'{self.text}' + '.', text_color='black')

    def btn_operation(self, entry, button, res):
        self.text = entry.cget('text')
        self.text_btn = button.cget('text')
        self.text_res = res.cget('text')
        self.number = 0.0
        if re.fullmatch(r"\d*\.\d*", self.text) or re.fullmatch(r"\d+", self.text):
            if self.text == '.':
                self.number = 0.0
            else:
                self.number = float(self.text)
        self.numbers.append(self.number)
        entry.configure(text = '')
        if self.text_btn == '+':
            self.operator = 1
            res.configure(text = f'{self.text_res}' + f'{self.number} +')
        if self.text_btn == '-':
            self.operator = 2
            res.configure(text = f'{self.text_res}' + f'{self.number} -')
        if self.text_btn == '/':
            self.operator = 3
            res.configure(text = f'{self.text_res}' + f'{self.number} /')
        if self.text_btn == '*':
            self.operator = 4
            res.configure(text = f'{self.text_res}' + f'{self.number} *')
        if self.text_btn == '2^--x':
            self.operator = 5
            res.configure(text = f'{self.text_res}' + f'{self.number} ^rad2')
            self.ansewr = str(self.do.operate(self.operator, self.numbers))
            entry.configure(text = self.ansewr)
        if self.text_btn == 'x^2':
            self.operator = 6
            res.configure(text = f'{self.text_res}' + f'{self.number} ^2')
            self.ansewr = str(self.do.operate(self.operator, self.numbers))
            entry.configure(text = self.ansewr)
        if self.text_btn == '1/x':
            self.operator = 7
            res.configure(text = f'1/{self.number}')
            self.ansewr = str(self.do.operate(self.operator, self.numbers))
            entry.configure(text = self.ansewr)
        if self.text_btn == '+/-':
            self.operator = 8
            res.configure(text = f'')
            self.ansewr = str(self.do.operate(self.operator, self.numbers))
            entry.configure(text = self.ansewr)
            

    def btn_quality(self, entry, res):
        self.text = entry.cget('text')
        self.number = 0.0
        if re.fullmatch(r"\d*\.\d*", self.text) or re.fullmatch(r"\d+", self.text):
            if self.text == '.':
                self.number = 0.0
            else:
                self.number = float(self.text)
        self.numbers.append(self.number)
        self.text_res = res.cget('text')
        res.configure(text = f'{self.text_res}' + f' {self.number} =')
        self.ansewr = str(self.do.operate(self.operator, self.numbers))
        entry.configure(text = self.ansewr)
        self.numbers = []
    
    def clear_btn(self, entry, res):
        entry.configure(text='')
        res.configure(text='')
        self.numbers = []


class Get():
    def __init__(self):
        self.obj = Operate()

    def operate(self, operator, numbers):
        swith ={
            1:self.obj.add,
            2:self.obj.sub,
            3:self.obj.div,
            4:self.obj.mul,
            5:self.obj.rad,
            6:self.obj.my_pow,
            7:self.obj.ded,
            8:self.obj.cor
        }
        fun = swith.get(operator)
        self.ansewr = fun(numbers)
        return self.ansewr
