import tkinter as tk
#Doku:
# https://docs.python.org/3/library/tkinter.html#tkinter-basic-mapping
# ref https://web.archive.org/web/20190524140835/https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html



class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid(column=2,row=3, sticky=tk.N+tk.S+tk.E+tk.W ) #erzeugt ein mastergrid
        self.columnconfigure(0, weight = 1) #grid setting
        self.rowconfigure(0, weight = 1) #grid setting
        self.pack(pady = 100, padx = 100) #pady/x = Pixels ausserhalb hinzigefügt werden

#        self.pack()
        self.create_variables()
        self.create_widgets()
        self.updater()


    def create_variables(self):
        self.choices = [ 'Pizza','Lasagne','Fries','Fish','Potatoe']
        self.dropvar = tk.StringVar() #Erzeugt eine Variable nutzbar für tk
        self.dropvar.set(self.choices[0]) # set setzt die Variable, .get liest sie aus, zv bei OptionMenu
        self.textvar = tk.StringVar()
        self.dropvar.trace("w", self.read_list) #.trace r/w/u für read/write/undefine, callback muss eine funktion sein
        
        


#        self.choices = [ 'Pizza','Lasagne','Fries','Fish','Potatoe']
#        self.textvar = tk.StringVar() 
#        self.dropvar.set(self.choices[0]) 


    def read_list(self,*args):
        self.textvar.set(self.dropvar.get())
        print(self.textvar.get())



    def create_widgets(self):
        self.text1 = tk.Label(self, text="Text hier !").grid(row = 1, column = 1, sticky="e")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "New Item"
        self.hi_there["width"] = "20"
        self.hi_there["command"] = self.add_column
        self.hi_there.grid(row = 1, column = 2,sticky="w") #wenn ein grid benutzt wird, kein .pack notwendig
#        self.hi_there.pack(side="top") #wenn ein grid benutzt wird, kein .pack notwendig

        self.hi_there_2 = tk.Button(self)
        self.hi_there_2["text"] = "Hello World 2 \n(click me)"
        self.hi_there_2["command"] = self.say_hi
        self.hi_there_2.grid(row = 1, column = 3,sticky="e")
#        self.hi_there_2.pack(side="right")

        self.DropMenu = tk.OptionMenu(self, self.dropvar, *self.choices) #args: erstauswahl, liste. * für Einträge aus liste
        self.DropMenu.grid(row = 2, column = 1,sticky="e")
#        self.DropMenu.pack(side="left")
        
        self.text2 = tk.Label(self, textvariable=self.textvar).grid(row = 2, column = 2, sticky="e")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row = 3, column = 3,sticky="e")
#        self.quit.pack(side="left")

    def updater(self):
        # updater gets called every 500 msec
        print("updater")

        root.after(500, self.updater)


    def add_column(self):
        self.grid(column=1,row=3, sticky="n" ) #erzeugt ein mastergrid
        self.DropMenu1 = tk.OptionMenu(self, self.dropvar, *self.choices) #args: erstauswahl, liste. * für Einträge aus liste
        self.DropMenu1.grid(row = 1, column = 1,sticky="e")




    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
