import tkinter as tk
#Doku:
# https://docs.python.org/3/library/tkinter.html#tkinter-basic-mapping


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["width"] = "80"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.hi_there_2 = tk.Button(self)
        self.hi_there_2["text"] = "Hello World 2 \n(click me)"
        self.hi_there_2["command"] = self.say_hi
        self.hi_there_2.pack(side="right")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="left")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
