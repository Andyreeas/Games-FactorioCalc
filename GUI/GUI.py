# Import GUI
import tkinter as tk 
#Extend Path, for Importing Module in Parent
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
# Import from folder calcs
from calcs import getValues

#Doku:
# https://docs.python.org/3/library/tkinter.html#tkinter-basic-mapping
# ref https://web.archive.org/web/20190524140835/https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# ref grid/frame https://stackoverflow.com/questions/36506152/tkinter-grid-or-pack-inside-a-grid


#To Do
# Button pro Line für Delete
# Del Button bei leerer Liste
# Stardarts für Fliesband, Montage-geschwindigkeit
# Ungerade Indexe bei listen von Calc => Wert





class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        # -------------------------------
        # Create a new Frame
        self.menue_top = tk.Frame(root, width=300)
        self.menue_top.grid(row=0, column=0, sticky="nsew")
        self.menue_top.pack(pady = 30, padx = 30)
        # Configure Column "5", min. size 
        self.menue_top.columnconfigure(5,minsize=100, weight = 1) 
        self.menue_top.rowconfigure(0, weight = 1) #grid setting
        # -------------------------------
        # Load variables and create all widgets
        self.load_variables()
        self.create_widgets()


    def load_variables(self):
        #   Create Object from Import
        db = getValues.getValues()
        #Load variables as a list from folder "calcs", file "getValues"
        self.db_list = db.getAllItemNames()
           # choices defines de dropdownmenu list
        self.choices = self.db_list
           # list_dropvar holds the active value from the dropdownmenu
        self.list_dropvar = [] 
           # list_dropmenu holds all the dropmenu widgets, [0] equals row"2"
        self.list_dropmenu = []
           # list_item_time holds all the Label widgets for "time"
        self.list_item_time = []
           # list_item_time_var holds the "time" value of the corresponding "list_dropvar"
        self.list_item_time_var = []
           # search_key needs to be initialized as StringVar, holds the search variable
        self.search_key = tk.StringVar()
           # listcount Counter for the Rows
        self.listcount = 2
        
        
    def create_widgets(self):
        # Column label description
        self.label_time = tk.Label(self.menue_top, text="Time").grid(
                                   row = 1, column = 2, sticky="e")
        self.label_search = tk.Label(self.menue_top, text=("Suche:")).grid(
                                   row = 0, column = 3, sticky="w")
        # -------------------------------
        # Top Buttons
        self.searchbox = tk.Entry(self.menue_top, textvariable=self.search_key).grid(
                                  row = 0, column = 4,sticky="e")
        self.button_go_search = tk.Button(self.menue_top, text="Suche in neuer Zeile",
                                          command=self.search_engine).grid(
                                          row = 0, column = 5,sticky="e")
        self.button_del_row = tk.Button(self.menue_top, text="Lezte Zeile löschen",
                                        fg="red", command=self.del_line).grid(
                                        row = 0, column = 6,sticky="e")
        self.quit = tk.Button(self.menue_top, text="QUIT", fg="red",
                              command=self.master.destroy).grid(
                              row = 0, column = 7,sticky="e")
        # -------------------------------
        # First initial row
        self.add_line()
        # -------------------------------


    def add_line(self):
        # Adds a new row with:
        # list_dropvar initialized as a StringVar, and set value to first in choices
        self.list_dropvar.append(tk.StringVar())
        try:
            self.list_dropvar[-1].set(self.choices[0])
        except:
            self.list_dropvar[-1].set("Kein Eintrag")
        # list_item_time_var initialized as a StringVar, get value in read_items()
        self.list_item_time_var.append(tk.StringVar())
        #list_dropvar[-1] gets traced, if it get changed it changes all the Label variables
        self.list_dropvar[-1].trace("w", self.read_items)
        #Label-Widget for the list_item_time_var
        self.list_item_time.append(tk.Label(self.menue_top, textvariable=self.list_item_time_var[-1]))
        self.list_item_time[-1].grid( row = self.listcount, column = 2, sticky="w")
        # Creates dropdownmenu. #Eintrag [0] ist text2 (self.listcount: 2)
        self.list_dropmenu.append(tk.OptionMenu(self.menue_top, self.list_dropvar[-1],
                                                *self.choices if not self.choices == [] else "" ))
        self.list_dropmenu[-1].grid(row = self.listcount, column = 1,sticky="w")
        # -------------------------------
        self.listcount += 1
    

    def del_line(self):
        #Deletes the Widget and .pop the list
        if self.listcount > 2:
            self.list_item_time[-1].grid_forget()
            self.list_item_time.pop()
            self.list_dropmenu[-1].grid_forget()
            self.list_dropmenu.pop()
            self.listcount -= 1
        else:
            print("nothing to delete")


    def read_items(self,*args):
        # If de Dropmenu Variable(list_dropvar) changes, change all the corresponding Label texts
        self.list_item_time_var[-1].set(db.getTime(self.list_dropvar[-1].get()))


    def search_engine(self):
        # search the db_list with the search_key, append it to choices and generate a new row
        self.choices = []
        # get the smallcaps value of the search_key, and merge the letters
        search_var = str("".join([x.lower() for x in self.search_key.get()]))
        if len(search_var) != 0:
            for text in [x.lower() for x in self.db_list]:
                if search_var in text:
                    print(self.choices)
                    self.choices.append(text)
        else:
            self.choices = self.db_list
        self.add_line()
                


root = tk.Tk()
app = Application(master=root)
app.mainloop()
