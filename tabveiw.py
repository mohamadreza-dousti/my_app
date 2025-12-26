import customtkinter as ctk

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('CREATED BY DOUSTI')
        self.geometry('400x400')

        self.tabview = ctk.CTkTabview(self, width=380, height=280,
                                corner_radius=15)
        self.tabview.pack(padx=10, pady=10, fill='both',
                    expand=True)

        self.tab1 = self.tabview.add('Calculator')
        self.tab2 = self.tabview.add('Temperature')