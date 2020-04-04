# Import GUI
import tkinter as tk 

from ..calcs import calcs

#Doku:
# https://docs.python.org/3/library/tkinter.html#tkinter-basic-mapping
# ref https://web.archive.org/web/20190524140835/https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# ref grid/frame https://stackoverflow.com/questions/36506152/tkinter-grid-or-pack-inside-a-grid

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.menue_top = tk.Frame(root, width=300)
        self.menue_top.grid(row=0, column=0, sticky="nsew")
        self.menue_top.pack(pady = 30, padx = 30)
        self.menue_top.columnconfigure(5,minsize=100, weight = 1) #grid setting
        self.menue_top.rowconfigure(0, weight = 1) #grid setting

        self.load_variables()
        self.create_widgets()


    def load_variables(self):

        self.db_list = [ 'Pizza','Lasagne','Fries','Fish','Potatoe']
#        self.choices = [ 'Pizza','Lasagne','Fries','Fish','Potatoe']
        self.choices = self.db_list
        self.list_text = [] #Eintrag [0] ist text1
        self.list_dropvar = []
        self.list_dropmenu = []
        self.list_textvar = []

        print(calcs().get_allItemNames())

        self.search_key = tk.StringVar()
        self.listcount = 1
        
        

    def create_widgets(self):
        self.add_line() #initial line

        textsuche = tk.Label(self.menue_top, text=("Suche:")).grid( row = 0, column = 3, sticky="w")
        self.searchbox = tk.Entry(self.menue_top, textvariable=self.search_key)
        self.searchbox.grid(row = 0, column = 4,sticky="e")
        self.button_go_search = tk.Button(self.menue_top, text="los finde!", #IMMER SCHÖN MAINFRAME ALS PARENT
                              command=self.search_engine)
        self.button_go_search.grid(row = 0, column = 6,sticky="e")

        self.add_row = tk.Button(self.menue_top, text="Neue Zeile", #IMMER SCHÖN MAINFRAME ALS PARENT
                              command=self.add_line)
        self.add_row.grid(row = 0, column = 1,sticky="e")





        self.quit = tk.Button(self.menue_top, text="QUIT", fg="red",
                              command=self.master.destroy)
#        self.quit.pack(side="left")
        self.quit.grid(row = 0, column = 7,sticky="e")


        

    def add_line(self):
        self.list_text.append(tk.Label(self.menue_top, text=("text",self.listcount)).grid( row = self.listcount, column = 2, sticky="w"))

        #Erstellt das Dropdown menu für jede Zeile. #Eintrag [0] ist text1 (self.listcount: 1). 
        self.list_dropvar.append(tk.StringVar())
        try:
            self.list_dropvar[-1].set(self.choices[0])
        except:
            self.list_dropvar[-1].set("Kein Eintrag")
#        self.list_dropvar[-1].trace("w", self.read_list(count=self.listcount)) #.trace r/w/u für read/write/undefine, callback muss eine funktion sein
        self.list_dropmenu.append(tk.OptionMenu(self.menue_top, self.list_dropvar[-1],*self.choices if not self.choices == [] else "" )) #args: erstauswahl, liste. * für Einträge aus liste
        self.list_dropmenu[-1].grid(row = self.listcount, column = 1,sticky="w")
        print(self.list_dropvar[-1])
        
        self.listcount += 1
       

    def search_engine(self):
        print("search_engine")
        self.choices = []
        search_var = [x.lower() for x in self.search_key.get()]
        search_var_1 = str("".join(search_var))
        "".join(search_var)
        print("VAR......",search_var_1)
        if len(search_var) != 0:
            for text in [x.lower() for x in self.db_list]:
                if search_var_1 in text:
                    print(self.choices)
                    self.choices.append(text)
        else:
            self.choices = self.db_list
                

#    def read_list(self,*args, count=0):
#        self.list_textvar.append(self.list_dropvar[count].get())
#        print(self.textvar.get())


root = tk.Tk()
app = Application(master=root)
app.mainloop()
