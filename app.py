import risk_funcs
import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 9)

class RiskAssist(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        s=ttk.Style()
        s.theme_use('clam')

        tk.Tk.wm_title(self, "Risk Assist")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for window in (MainMenu, SingleRoll, BattleSim):
            frame = window(container, self)
            self.frames[window] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.config(bg='white')
        
        self.show_frame(MainMenu)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainMenu(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # frame header
        label = tk.Label(self, text="Main Menu", font=LARGE_FONT, bg='white')
        label.grid(pady=10, padx=10)
        
        # link to single roll frame
        button1 = ttk.Button(self, text="Single Roll",
                             command=lambda: controller.show_frame(SingleRoll))
        button1.grid(pady=10,padx=10)
        
        # link to battle sim frame
        button2 = ttk.Button(self, text="Battle Sim",
                             command=lambda: controller.show_frame(BattleSim))
        button2.grid(pady=10,padx=10)
        
class SingleRoll(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # frame header
        label1 = tk.Label(self, text="Single Roll", font=LARGE_FONT, bg='white')
        label1.grid(row=0)
        
        # entry header
        label2 = tk.Label(self, text="Number of dice", bg='white')
        label2.grid(row=1,column=1,pady=5,padx=5)
        
        # row for attacker entry
        label3 = tk.Label(self, text="Attacker:", bg='white')
        label3.grid(row=2,column=0,sticky='w',pady=5,padx=5)
        entry1 = ttk.Entry(self,width=5)
        entry1.grid(row=2,column=1,pady=5,padx=5)
        
        # row for defender entry
        label4 = tk.Label(self, text="Defender:", bg='white')
        label4.grid(row=3, column=0,sticky='w',pady=5,padx=5)
        entry2 = ttk.Entry(self,width=5)
        entry2.grid(row=3,column=1,pady=5,padx=5)
        
        # calculate single roll outcome
        button1 = ttk.Button(self, text="Enter",
                             command=lambda: risk_funcs.single_roll(int(entry1.get()), 
                                                                    int(entry2.get())))
        button1.grid(row=4,column=0,sticky='w',pady=5,padx=5)
        
        # back to main menu
        button2 = ttk.Button(self, text="Main Menu",
                             command=lambda: controller.show_frame(MainMenu))
        button2.grid(row=4,column=1,sticky='e',pady=5,padx=5)
        
class BattleSim(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # frame header
        label1 = tk.Label(self, text="Battle Sim", font=LARGE_FONT, bg='white')
        label1.grid(row=0)
        
        # entry header
        label2 = tk.Label(self, text="Number of units", bg='white')
        label2.grid(row=1,column=1,pady=5,padx=5)
        
        # row for attacker entry
        label3 = tk.Label(self, text="Attacker:", bg='white')
        label3.grid(row=2,column=0,sticky='w',pady=5,padx=5)
        entry1 = ttk.Entry(self,width=5)
        entry1.grid(row=2,column=1,pady=5,padx=5)
        
        # row for defender entry
        label4 = tk.Label(self, text="Defender:", bg='white')
        label4.grid(row=3, column=0,sticky='w',pady=5,padx=5)
        entry2 = ttk.Entry(self,width=5)
        entry2.grid(row=3,column=1,pady=5,padx=5)
        
        # calculate single roll outcome
        button1 = ttk.Button(self, text="Enter",
                             command=lambda: risk_funcs.battle_sim(int(entry1.get()), 
                                                                   int(entry2.get())))
        button1.grid(row=4,column=0,sticky='w',pady=5,padx=5)
        
        # back to main menu
        button2 = ttk.Button(self, text="Main Menu", 
                             command=lambda: controller.show_frame(MainMenu))
        button2.grid(row=4,column=1,sticky='e',pady=5,padx=5)

app = RiskAssist()
app.mainloop()
