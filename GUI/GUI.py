import tkinter as tk
#Doku:
# https://docs.python.org/3/library/tkinter.html#tkinter-basic-mapping
# ref https://web.archive.org/web/20190524140835/https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# ref grid/frame https://stackoverflow.com/questions/36506152/tkinter-grid-or-pack-inside-a-grid

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.menue_top = tk.Frame(root, width=300)
        self.menue_top.grid(row=1, column=1, sticky="nsew")
        self.list_frame = tk.Frame(master)
        self.list_frame.pack(expand=True,)







        self.create_variables()
        self.create_widgets()


    def create_variables(self):
        pass
        

    def create_widgets(self):
        self.quit = tk.Button(self.menue_top, text="QUIT", fg="red",
                              command=self.master.destroy)
#        self.quit.pack(side="left")
        self.quit.grid(row = 1, column = 1,sticky="e")



        pass


root = tk.Tk()
app = Application(master=root)
app.mainloop()
