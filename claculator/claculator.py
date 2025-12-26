import customtkinter as ctk
from tabs.tabveiw import Main
from claculator.app_calculator import AppCalculator


class Calculator(Main):
    def __init__(self):
        super().__init__()
        self.manage_cal = AppCalculator()

        self.res_lable = ctk.CTkLabel(self.tab1, width=375, height=20, text='')
        self.res_lable.pack()

        self.ansewr_lable = ctk.CTkLabel(self.tab1, width=375, height=40, corner_radius=15,
                                   fg_color='gray', text='', text_color='black')
        self.ansewr_lable.pack(pady=10)

        self.frame = ctk.CTkFrame(self.tab1)
        self.frame.pack(pady=20)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_columnconfigure(3, weight=1)

        self.deduction_btn = ctk.CTkButton(self.frame, text='1/x',
                                    corner_radius=5, fg_color='black',
                                    command=lambda:self.manage_cal.btn_operation(self.ansewr_lable, self.deduction_btn, self.res_lable))
        self.deduction_btn.grid(row = 0, column = 0)

        self.power_btn = ctk.CTkButton(self.frame, text='x^2', corner_radius=5,
                                fg_color='black',
                                command=lambda:self.manage_cal.btn_operation(self.ansewr_lable, self.power_btn, self.res_lable))
        self.power_btn.grid(row = 0, column = 1)

        self.radical_btn = ctk.CTkButton(self.frame, text='2^--x',
                                    corner_radius=5, fg_color='black', 
                                    command=lambda:self.manage_cal.btn_operation(self.ansewr_lable, self.radical_btn, self.res_lable))
        self.radical_btn.grid(row = 0, column = 2)

        self.division_btn = ctk.CTkButton(self.frame, text='/', corner_radius=5, 
                                    fg_color='black', command=lambda:self.manage_cal.btn_operation(self.ansewr_lable, self.division_btn, self.res_lable))
        self.division_btn.grid(row = 0, column = 3)

        self.btn1 = ctk.CTkButton(self.frame, text='1', corner_radius=5,
                            fg_color='black', command=lambda:self.manage_cal.btn_number(self.ansewr_lable, self.btn1))
        self.btn1.grid(row = 1, column = 0)

        self.btn2 = ctk.CTkButton(self.frame, text='2', corner_radius=5,
                            fg_color='black', command=lambda:self.manage_cal.btn_number(self.ansewr_lable, self.btn2))
        self.btn2.grid(row = 1, column = 1)

        self.btn3 = ctk.CTkButton(self.frame, text='3', corner_radius=5,
                            fg_color='black', command=lambda:self.manage_cal.btn_number(self.ansewr_lable, self.btn3))
        self.btn3.grid(row = 1, column = 2)

        self.multi_btn = ctk.CTkButton(self.frame, text='*', corner_radius=5, 
                                fg_color='black', command=lambda:self.manage_cal.btn_operation(self.ansewr_lable, self.multi_btn, self.res_lable))
        self.multi_btn.grid(row = 1, column = 3)

        self.btn4 = ctk.CTkButton(self.frame, text='4', corner_radius=5,
                            fg_color='black', command=lambda:self.manage_cal.btn_number(self.ansewr_lable, self.btn4))
        self.btn4.grid(row = 2, column = 0)

        self.btn5 = ctk.CTkButton(self.frame, text='5', corner_radius=5,
                            fg_color='black', command=lambda:self.manage_cal.btn_number(self.ansewr_lable, self.btn5))
        self.btn5.grid(row = 2, column = 1)

        self.btn6 = ctk.CTkButton(self.frame, text='6', corner_radius=5,
                            fg_color='black', command=lambda:self.manage_cal.btn_number(self.ansewr_lable, self.btn6))
        self.btn6.grid(row = 2, column = 2)

        self.mines_btn = ctk.CTkButton(self.frame, text='-', corner_radius=5, 
                                fg_color='black', command=lambda:self.manage_cal.btn_operation(self.ansewr_lable, self.mines_btn, self.res_lable))
        self.mines_btn.grid(row = 2, column = 3)

        self.btn7 = ctk.CTkButton(self.frame, text='7', corner_radius=5,
                         fg_color='black', command=lambda:self.manage_cal.btn_number(self.ansewr_lable, self.btn7))
        self.btn7.grid(row = 3, column = 0)

        self.btn8 = ctk.CTkButton(self.frame, text='8', corner_radius=5,
                            fg_color='black', command=lambda:self.manage_cal.btn_number(self.ansewr_lable, self.btn8))
        self.btn8.grid(row = 3, column = 1)

        self.btn9 = ctk.CTkButton(self.frame, text='9', corner_radius=5,
                            fg_color='black', command=lambda:self.manage_cal.btn_number(self.ansewr_lable, self.btn9))
        self.btn9.grid(row = 3, column = 2)

        self.add_btn = ctk.CTkButton(self.frame, text='+', corner_radius=5, fg_color='black',
                                      command=lambda:self.manage_cal.btn_operation(self.ansewr_lable, self.add_btn, self.res_lable))
        self.add_btn.grid(row = 3, column = 3)

        self.negetive_btn = ctk.CTkButton(self.frame, text='+/-', corner_radius=5,
                                     fg_color='black', 
                                     command=lambda:self.manage_cal.btn_operation(self.ansewr_lable, self.negetive_btn, self.res_lable))
        self.negetive_btn.grid(row = 4, column = 0)

        self.btn0 = ctk.CTkButton(self.frame, text='0', corner_radius=5, 
                             fg_color='black', command=lambda:self.manage_cal.btn_number(self.ansewr_lable, self.btn0))
        self.btn0.grid(row = 4, column = 1)

        self.btn_dot = ctk.CTkButton(self.frame, text='.', corner_radius=5,
                                fg_color='black', command=lambda:self.manage_cal.btn_number(self.ansewr_lable, self.btn_dot))
        self.btn_dot.grid(row = 4, column = 2)

        self.btn_ansewr = ctk.CTkButton(self.frame, text='=', corner_radius=5,
                                   fg_color='blue', command=lambda:self.manage_cal.btn_quality(self.ansewr_lable, self.res_lable))
        self.btn_ansewr.grid(row = 4, column = 3)

        self.clear_btn = ctk.CTkButton(self.frame, text='Clear', fg_color='black', 
                                       corner_radius=15, command=lambda:self.manage_cal.clear_btn(self.ansewr_lable, self.res_lable))
        self.clear_btn.grid(row = 5, column = 3)