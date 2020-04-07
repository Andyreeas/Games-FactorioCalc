# Import
import tkinter as tk 
#Extend Path, for Importing Module in Parent
#import os,sys,inspect
#current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir) 
# Import from folder calcs
from calcs import getValues
from calcs import calcPR

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
        self.menue_top.columnconfigure(3,minsize=10, weight = 1)
        self.menue_top.columnconfigure(9,minsize=30, weight = 1) 
        self.menue_top.rowconfigure(0, weight = 1) #grid setting
        # -------------------------------
        # Load variables and create all widgets
        self.load_variables()
        self.create_widgets()
        self.updater()



    def load_variables(self):
        #   Create Object from Import
        self.db = getValues.getValues()
        self.pr = calcPR.calcPR()
        #Load variables as a list from folder "calcs", file "getValues"
        self.db_list = self.db.getAllItemNames()
           # choices defines de dropdownmenu list
        self.choices = self.db_list
           # list_dropvar holds the active value from the dropdownmenu
        self.list_dropvar = [] 
           # list_dropmenu holds all the dropmenu widgets, [0] equals row"3"
        self.list_dropmenu = []
        # -------------------------------
        # INPUT LISTS
        self.list_speed = []
        self.list_speed_v = []
        self.list_eff = []
        self.list_eff_v = []
        self.list_energy = []
        self.list_energy_v = []
        self.list_speed_bea = []
        self.list_speed_bea_V = []
        self.list_eff_bea = []
        self.list_eff_bea_V = []
        self.list_energy_bea = []
        self.list_energy_bea_V = []
        self.lsit_ipm_in = []
        self.lsit_ipm_in_V = []
        # -------------------------------
        # OUTPUT LISTS
           # list_item_time holds all the Label widgets for "time"
#        self.list_item_time = []

        #self.list_ips_out = []
        self.list_fullb = []
        self.list_buildam = []

        # -------------------------------
           # list_item_time_var holds the "time" value of the corresponding "list_dropvar"
        self.search_key = tk.StringVar()
           # listcount Counter for the Rows
        self.listcount = 3
        
        
    def create_widgets(self):
        print("create_widget")
        # Column label description
        # Top Buttons
        self.label_search = tk.Label(self.menue_top, text="Suche:").grid(
                                   row = 0, column = 2, sticky="w")
        self.searchbox = tk.Entry(self.menue_top, textvariable=self.search_key, width=15).grid(
                                  row = 0, column = 3,columnspan=2, sticky="e")
        self.button_go_search = tk.Button(self.menue_top, text="Suche in neuer Zeile",
                                          command=self.search_engine).grid(
                                          row = 0, column = 5,columnspan=3, sticky="e")
        self.button_del_row = tk.Button(self.menue_top, text="Lezte Zeile löschen",
                                        fg="red", command=self.del_line).grid(
                                        row = 0, column = 8, columnspan=2, sticky="e")
        self.quit = tk.Button(self.menue_top, text="QUIT", fg="red",
                              command=self.master.destroy).grid(
                              row = 0, column = 10,sticky="e")
        # -------------------------------
        self.label_booster = tk.Label(self.menue_top, text="Booster", bg="#dec8c3").grid(
                                   row = 1, column = 2,columnspan=3, sticky="n")
        self.label_speed = tk.Label(self.menue_top, text="Speed", bg="#dec8c3").grid(
                                   row = 2, column = 2, sticky="e")
        self.label_eff = tk.Label(self.menue_top, text="Efficiency", bg="#dec8c3").grid(
                                   row = 2, column = 3, sticky="e")
        self.label_energy = tk.Label(self.menue_top, text="Energy", bg="#dec8c3").grid(
                                   row = 2, column = 4, sticky="e")
        # -------------------------------
        self.label_booster_bea = tk.Label(self.menue_top, text="Booster Beacon", bg="#c3cade").grid(
                                   row = 1, column = 5,columnspan=3, sticky="n")
        self.label_speed_bea = tk.Label(self.menue_top, text="Speed", bg="#c3cade").grid(
                                   row = 2, column = 5, sticky="n")
        self.label_eff_bea = tk.Label(self.menue_top, text="Efficiency", bg="#c3cade").grid(
                                   row = 2, column = 6, sticky="e")
        self.label_energy_bea = tk.Label(self.menue_top, text="Energy", bg="#c3cade").grid(
                                   row = 2, column = 7, sticky="e")
        # -------------------------------
        self.label_in_ipm = tk.Label(self.menue_top, text="Items/min").grid(
                                   row = 2, column = 8, sticky="n")
        # -------------------------------
        self.label_out_ips = tk.Label(self.menue_top, text="Items/sec").grid(
                                   row = 2, column = 10, sticky="n")
        self.label_out_fullb = tk.Label(self.menue_top, text="full belt").grid(
                                   row = 2, column = 11, sticky="n")
        self.label_time = tk.Label(self.menue_top, text="Time").grid(
                                   row = 2, column = 12, sticky="e")
        # -------------------------------
        # First initial row
        self.add_line()
        # -------------------------------



    def updater(self):
        # updates the text Labels
        #print("updater")
        for i in range(self.listcount -3):
#            self.list_item_time[i].config(text=self.db.getTime(self.list_dropvar[i].get()))
            self.list_fullb[i].config(text=self.pr.builderFullBelt(45, self.list_dropvar[-1].get(),1.25, 0,0,0,0,0,0,0,0,0,0,0,))
        root.after(500, self.updater)



    def add_line(self):
        # Adds a new row with:
        # list_dropvar initialized as a StringVar, and set value to first in choices
        self.list_dropvar.append(tk.StringVar())
        try:
            self.list_dropvar[self.listcount -3].set(self.choices[0])
        except:
            self.list_dropvar[self.listcount -3].set("Kein Eintrag")
        # -------------------------------
        #Label-Widget for the list_item_time_var
#        self.list_item_time.append(tk.Label(self.menue_top, text=self.db.getTime(self.list_dropvar[-1].get())))
#        self.list_item_time[-1].grid( row = self.listcount, column = 12, sticky="w")
        # Creates dropdownmenu. #Eintrag [0] ist text2 (self.listcount: 2)
        self.list_dropmenu.append(tk.OptionMenu(self.menue_top, self.list_dropvar[-1],
                                                *self.choices if not self.choices == [] else "" ))
        self.list_dropmenu[-1].grid(row = self.listcount, column = 1,sticky="w")
        # -------------------------------
        # Input Lists
        self.list_speed_v.append(tk.StringVar())
        self.list_speed.append(tk.Entry(self.menue_top, textvariable=self.list_speed_v,width=2).grid(
                                        row = self.listcount, column = 2, sticky="n"))
        self.list_eff.append(tk.StringVar())
        self.list_eff.append(tk.Entry(self.menue_top, textvariable=self.list_eff_v,width=2).grid(
                                      row = self.listcount, column = 3, sticky="n"))


        # -------------------------------
        # Output Lists
        self.list_fullb.append(tk.Label(self.menue_top, text=self.pr.builderFullBelt(45, self.list_dropvar[-1].get(),1.25, 0,0,0,0,0,0,0,0,0,0,0,)))
                                            
        self.list_fullb[-1].grid(row = self.listcount, column = 11, sticky="n")

        # -------------------------------
        self.listcount += 1
        



    

    def del_line(self):
        #Deletes the Widget and .pop the list
        if self.listcount > 3:
            self.list_item_time[-1].grid_forget()
            self.list_item_time.pop()
            self.list_dropvar.pop(-1)
            self.list_dropmenu[-1].grid_forget()
            self.list_dropmenu.pop()
            self.listcount -= 1

        else:
            print("nothing to delete")


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
app.title = "Factorio Calc"
root.mainloop()

print("mainloop out, Exit")
