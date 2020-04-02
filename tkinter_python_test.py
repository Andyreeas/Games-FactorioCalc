import tkinter as tk
#Doku:
# https://docs.python.org/3/library/tkinter.html#tkinter-basic-mapping
# ref https://web.archive.org/web/20190524140835/https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(column=2,row=3, sticky="n" ) #erzeugt ein mastergrid
        self.columnconfigure(0, weight = 1) #grid setting
        self.rowconfigure(0, weight = 1) #grid setting
        self.pack(pady = 100, padx = 100) #pady/x = Minimum grösse

#        self.pack()
        self.create_variables()
        self.create_widgets()

    def create_variables(self):
        self.choices = [ 'Pizza','Lasagne','Fries','Fish','Potatoe']
        self.dropvar = tk.StringVar() #Erzeugt eine Variable nutzbar für tk
        self.dropvar.set(self.choices[0]) # set setzt die Variable, .get liest sie aus, zv bei OptionMenu
        self.dropvar.trace("w", self.read_list) #.trace r/w/u für read/write/undefine, callback muss eine funktion sein
        self.textvar = tk.StringVar()
        self.textvar = self.dropvar.get()

#        self.choices = [ 'Pizza','Lasagne','Fries','Fish','Potatoe']
#        self.textvar = tk.StringVar() 
#        self.dropvar.set(self.choices[0]) 


    def read_list(self):
        self.textvar = self.dropvar.get()
        print(textvar)
        
        

    def create_widgets(self):
        self.text1 = tk.Label(self, text="Text hier !").grid(row = 1, column = 1, sticky="e")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["width"] = "80"
        self.hi_there["command"] = self.say_hi
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
        

        self.text2 = tk.Label(self, text=self.textvar).grid(row = 2, column = 2, sticky="e")


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row = 3, column = 3,sticky="e")
#        self.quit.pack(side="left")


    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
