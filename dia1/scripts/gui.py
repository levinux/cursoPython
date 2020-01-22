import tkinter as tk
from tkinter import messagebox


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.hi_there = tk.Button(self)
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there["text"] = "Click me!"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit.pack(side="bottom")

    def say_hi(self):
        messagebox.showinfo(message="Ola k ase?")


# Main
root = tk.Tk()
app = App(master=root)
app.mainloop()
