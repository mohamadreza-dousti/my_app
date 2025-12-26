import customtkinter as ctk
from claculator import Calculator
from app_temperature import AppTemperature

class Temperature(Calculator):
    def __init__(self):
        super().__init__()
        self.manage = AppTemperature()
        self.entry = ctk.CTkEntry(self.tab2, width=375, height=40,
                              placeholder_text="Amount")
        self.entry.pack(pady=15)

        self.frame_from = ctk.CTkFrame(self.tab2, width=375, height=30)
        self.frame_from.pack(pady=0)

        self.lable_from = ctk.CTkLabel(self.frame_from, text='FROM')
        self.lable_from.pack(side='left', pady=0)

        self.option = ['Celsius', 'Kelvin', 'Fahrenheit']

        self.option_var_from = ctk.StringVar(value='choose')
        self.check_from = ctk.CTkOptionMenu(self.tab2, width=375, height=40,
                                      values=self.option,
                                      variable=self.option_var_from,
                                      command=self.manage.get_check_from)
        self.check_from.pack(pady=0)

        self.option_var_to = ctk.StringVar(value='choose')

        self.frame_to = ctk.CTkFrame(self.tab2, width=375, height=30)
        self.frame_to.pack(pady=0)

        self.lable_to = ctk.CTkLabel(self.frame_to, text='TO')
        self.lable_to.pack(side='left', pady=0)

        self.check_to = ctk.CTkOptionMenu(self.tab2, width=375, height=40,
                                      values=self.option,
                                      variable=self.option_var_to, command=self.manage.get_check_to)
        self.check_to.pack(pady=0)

        self.apply_btn = ctk.CTkButton(self.tab2, text='Apply', fg_color='black',
                                        command=lambda:self.manage.apply(self.entry, self.result))
        self.apply_btn.pack(pady=10)

        self.result = ctk.CTkLabel(self.tab2, text='', fg_color='white',
                                   width=375, height=60)
        self.result.pack(pady=0)