# Import
import tkinter as tk 
#Extend Path, for Importing Module in Parent
# Import from folder calcs
from calcs import getValues
from calcs import calcPR

#Doku:
# https://docs.python.org/3/library/tkinter.html#tkinter-basic-mapping
# ref https://web.archive.org/web/20190524140835/https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# ref grid/frame https://stackoverflow.com/questions/36506152/tkinter-grid-or-pack-inside-a-grid


#To Do:
# - True deleting system. Right now, only widgets get removed (.grid_forget()). Lists continue with "rowcount". PERFORMANCE?
# exeption Input IPM, buchstabe



class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        # -------------------------------
        # Create a new Frame
        self.menue_top = tk.Frame(root, width=700,height=300)
        self.menue_top.grid(row=0, column=0, sticky="nsew")
        self.menue_top.pack(pady = 30, padx = 30)
        # Configure Column "3,9", min. size 
        self.menue_top.columnconfigure(3,minsize=10, weight = 1)
        self.menue_top.columnconfigure(9,minsize=30, weight = 1) 
        self.menue_top.rowconfigure(0) #grid setting
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
        self.choices_modules = ["None"] + self.db.getModuleNames()
        self.choices_builder = self.db.getBuilderNames() #["Assembler 1","Assembler 2","Assembler 3","Furnance 1","Furnance 2,E","Chemicalplant","Raffinery","Centrifuge","Oilpump",]
        self.choices_belt = self.db.getBeltNames() #["Yellow","Red","Blue",]
           # list_dropvar holds the active value from the dropdownmenu
        self.list_dropvar = [] 
           # list_dropmenu holds all the dropmenu widgets, [0] equals row"3"
        self.list_dropmenu = []
        # -------------------------------
        self.list_del_button = []
        # INPUT LISTS
        # List are 2-D, [i][0]: dropvar, [i][1]: dropmenu
        self.list_builder = []
        self.list_belt = []
        self.list_ipm_in = []
        self.list_booster_1 = []
        self.list_booster_2 = []
        self.list_booster_3 = []
        self.list_booster_4 = []
        self.list_b_booster_1 = []
        self.list_b_booster_am = []
        self.list_var_sum = []
        # -------------------------------
        # OUTPUT LISTS
        self.list_fullbelt = []
        self.list_buildam = []

        # -------------------------------
           # list_item_time_var holds the "time" value of the corresponding "list_dropvar"
        self.search_key = tk.StringVar()
        self.belttyp_var = tk.StringVar()
        self.belttyp_var.set(45.0)
        self.montagetyp_var = tk.StringVar()
        self.montagetyp_var.set(1.25)
           # listcount Counter for the Rows
        self.rowcount = 3
        # linecount, counts the actual showed widgets
        self.linecount = 0
        # counts the deletions
        self.delete_count = 0


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
                                          row = 0, column = 5,columnspan=3, sticky="w")
#        self.button_del_row = tk.Button(self.menue_top, text="Lezte Zeile löschen",
#                                        fg="red", command=self.del_last_line).grid(
#                                        row = 0, column = 8, columnspan=2, sticky="e")
#        self.quit = tk.Button(self.menue_top, text="QUIT", fg="red",
#                              command=self.master.destroy).grid(
#                              row = 0, column = 10,sticky="e")
        # -------------------------------
        self.label_builder = tk.Label(self.menue_top, text="Builder",).grid(
                                   row = 2, column = 2, sticky="n")
        self.label_belt = tk.Label(self.menue_top, text="Belt",).grid(
                                   row = 2, column = 3, sticky="n")
        self.label_in_ipm = tk.Label(self.menue_top, text="Items/min",).grid(
                                   row = 2, column = 4, sticky="n")
        self.label_booster = tk.Label(self.menue_top, 
             text="Booster",bg="#dec8c3", width=93).grid(row = 2, column = 5,columnspan=4, sticky="n")
        # -------------------------------
        self.label_bea = tk.Label(self.menue_top, text="Beacon", bg="#c3cade", width=23).grid(
                                   row = 2, column = 9, sticky="n")
        self.label_count_bea = tk.Label(self.menue_top, text="Amount", bg="#c3cade", width=6).grid(
                                   row = 2, column = 10, sticky="n")
        # -------------------------------
#        self.label_out_ipm = tk.Label(self.menue_top, text="Items/min").grid(
#                                   row = 2, column = 13, sticky="n")
        # -------------------------------
        self.label_full_belt = tk.Label(self.menue_top, text="Builder for full belt",bg="#dec8c3", width=15).grid(
                                   row = 2, column = 14, sticky="n")
        self.label_am_builder = tk.Label(self.menue_top, text="Amount builder",bg="#c3cade", width=15).grid(
                                   row = 2, column = 15, sticky="n")
        # -------------------------------
        # First initial row
        self.add_line()
        # -------------------------------

        

    def updater(self):
        # updates the text Labels
        print("updater, i = ", self.linecount)
        for i in range(self.rowcount -3):
            try:
                value_booster_am = float(self.list_b_booster_am[i][0].get())
            except ValueError:
                value_booster_am = 0.
            try:
                value_ipm_in = int(self.list_ipm_in[i][0].get())
            except ValueError:
                value_ipm_in = 0.

            print("ERRROOOORRR___",value_ipm_in,
                                                                       self.list_dropvar[i].get(),
                                                                       self.list_builder[i][0].get(),
                                                                       self.list_booster_1[i][0].get(),
                                                                       self.list_booster_2[i][0].get(),
                                                                       self.list_booster_3[i][0].get(),
                                                                       self.list_booster_4[i][0].get(),
                                                                       self.list_b_booster_1[i][0].get(),
                                                                       value_booster_am,)




            self.list_fullbelt[i][1].config(text=(self.pr.builderFullBelt(self.list_belt[i][0].get(),
                                                                       self.list_dropvar[i].get(),
                                                                       self.list_builder[i][0].get(),
                                                                       self.list_booster_1[i][0].get(),
                                                                       self.list_booster_2[i][0].get(),
                                                                       self.list_booster_3[i][0].get(),
                                                                       self.list_booster_4[i][0].get(),
                                                                       self.list_b_booster_1[i][0].get(),
                                                                       value_booster_am,
                                                                      )))


            self.list_buildam[i][1].config(text=(self.pr.builderAmount(value_ipm_in,
                                                                       self.list_dropvar[i].get(),
                                                                       self.list_builder[i][0].get(),
                                                                       self.list_booster_1[i][0].get(),
                                                                       self.list_booster_2[i][0].get(),
                                                                       self.list_booster_3[i][0].get(),
                                                                       self.list_booster_4[i][0].get(),
                                                                       self.list_b_booster_1[i][0].get(),
                                                                       value_booster_am,
                                                                      )))


        root.after(500, self.updater)



    def add_line(self):
        cline = self.rowcount -3
        print("Add_line, cline", cline)
        # Adds a new row with:
        # list_dropvar initialized as a StringVar, and set value to first in choices
        self.list_dropvar.append(tk.StringVar())
        try:
            self.list_dropvar[cline].set(self.choices[0])
        except:
            self.list_dropvar[cline].set("Kein Eintrag")
        # -------------------------------
        #Label-Widget for the list_item_time_var
#        self.list_item_time.append(tk.Label(self.menue_top, text=self.db.getTime(self.list_dropvar[-1].get())))
#        self.list_item_time[-1].grid( row = self.rowcount, column = 12, sticky="w")
        # Creates dropdownmenu. #Eintrag [0] ist text2 (self.rowcount: 2)
        self.list_dropmenu.append(tk.OptionMenu(self.menue_top, self.list_dropvar[-1],
                                                *self.choices if not self.choices == [] else "" ))
        self.list_dropmenu[-1].grid(row = self.rowcount, column = 1,sticky="e")

        # -------------------------------
        # del Button
        self.list_del_button.append(tk.Button(self.menue_top, text="X", fg="red",
                                          command=lambda row=cline: self.del_row_line(row)))
        self.list_del_button[cline].grid(row = self.rowcount, column = 0, sticky="w")
        # -------------------------------
        # Input Lists
        # Steps: 1. Add new listentry, 2. [i][0]: Variable, 3. Setting to Choice, 4. [i][1]: Widget, 5. Grid
        self.list_builder.append([])
        self.list_builder[cline].append(tk.StringVar())
        self.list_builder[cline][0].set(self.choices_builder[0])
        self.list_builder[cline].append(tk.OptionMenu(self.menue_top, self.list_builder[cline][0],
                                                     *self.choices_builder))
        self.list_builder[cline][1].grid(row = self.rowcount, column = 2, sticky="n")
        # -
        self.list_belt.append([])
        self.list_belt[cline].append(tk.StringVar())
        self.list_belt[cline][0].set(self.choices_belt[0])
        self.list_belt[cline].append(tk.OptionMenu(self.menue_top, self.list_belt[cline][0],
                                                     *self.choices_belt))
        self.list_belt[cline][1].grid(row = self.rowcount, column = 3, sticky="n")
        # -
        self.list_ipm_in.append([])
        self.list_ipm_in[cline].append(tk.StringVar())
        self.list_ipm_in[cline].append(tk.Entry(self.menue_top, textvariable=self.list_ipm_in[cline][0], width=2))
        self.list_ipm_in[cline][1].grid(row = self.rowcount, column = 4, sticky="n")
        # -
        self.list_booster_1.append([])
        self.list_booster_1[cline].append(tk.StringVar())
        self.list_booster_1[cline][0].set(self.choices_modules[0])
        self.list_booster_1[cline].append(tk.OptionMenu(self.menue_top, self.list_booster_1[cline][0],
                                                     *self.choices_modules))
        self.list_booster_1[cline][1].grid(row = self.rowcount, column = 5, sticky="n")
        # -
        self.list_booster_2.append([])
        self.list_booster_2[cline].append(tk.StringVar())
        self.list_booster_2[cline][0].set(self.choices_modules[0])
        self.list_booster_2[cline].append(tk.OptionMenu(self.menue_top, self.list_booster_2[cline][0],
                                                     *self.choices_modules))
        self.list_booster_2[cline][1].grid(row = self.rowcount, column = 6, sticky="n")
        # -
        self.list_booster_3.append([])
        self.list_booster_3[cline].append(tk.StringVar())
        self.list_booster_3[cline][0].set(self.choices_modules[0])
        self.list_booster_3[cline].append(tk.OptionMenu(self.menue_top, self.list_booster_3[cline][0],
                                                     *self.choices_modules))
        self.list_booster_3[cline][1].grid(row = self.rowcount, column = 7, sticky="n")
        # -
        self.list_booster_4.append([])
        self.list_booster_4[cline].append(tk.StringVar())
        self.list_booster_4[cline][0].set(self.choices_modules[0])
        self.list_booster_4[cline].append(tk.OptionMenu(self.menue_top, self.list_booster_4[cline][0],
                                                     *self.choices_modules))
        self.list_booster_4[cline][1].grid(row = self.rowcount, column = 8, sticky="n")
        # -
        self.list_b_booster_1.append([])
        self.list_b_booster_1[cline].append(tk.StringVar())
        self.list_b_booster_1[cline][0].set(self.choices_modules[0])
        self.list_b_booster_1[cline].append(tk.OptionMenu(self.menue_top, self.list_b_booster_1[cline][0],
                                                     *self.choices_modules))
        self.list_b_booster_1[cline][1].grid(row = self.rowcount, column = 9, sticky="n")
        # -
        self.list_b_booster_am.append([])
        self.list_b_booster_am[cline].append(tk.StringVar())
        self.list_b_booster_am[cline].append(tk.Entry(self.menue_top, textvariable=self.list_b_booster_am[cline][0], width=2))
        self.list_b_booster_am[cline][1].grid(row = self.rowcount, column = 10, sticky="n")
        # -
        self.list_var_sum.append([])
        # -------------------------------
        # Output Lists
        self.list_fullbelt.append([])
        self.list_fullbelt[cline].append(tk.StringVar())
        self.list_fullbelt[cline].append(tk.Label(self.menue_top, text=self.list_fullbelt[cline][0].get()))                                            
        self.list_fullbelt[cline][1].grid(row = self.rowcount, column = 14, sticky="n")
        # -
        self.list_buildam.append([])
        self.list_buildam[cline].append(tk.StringVar())
        self.list_buildam[cline].append(tk.Label(self.menue_top, text=self.list_buildam[cline][0].get()))                                            
        self.list_buildam[cline][1].grid(row = self.rowcount, column = 15, sticky="n")

        self.rowcount += 1
        self.linecount += 1



    

    def del_last_line(self):
        #Deletes the LAST Widget and .pop the list
        if self.rowcount > 3:
            self.list_del_button[-1].grid_forget()
#            self.list_del_button.pop()
            # -
 #           self.list_dropvar.pop(-1)
            self.list_dropmenu[-1].grid_forget()
#            self.list_dropmenu.pop()
            # -
            self.list_builder[-1][1].grid_forget()
#            self.list_builder.pop()
            self.list_belt[-1][1].grid_forget()
#            self.list_belt.pop()
            self.list_ipm_in[-1][1].grid_forget()
#            self.list_ipm_in.pop()
            self.list_booster_1[-1][1].grid_forget()
#            self.list_booster_1.pop()
            self.list_booster_2[-1][1].grid_forget()
#            self.list_booster_2.pop()
            self.list_booster_3[-1][1].grid_forget()
#            self.list_booster_3.pop()
            self.list_booster_4[-1][1].grid_forget()
#            self.list_booster_4.pop()
            self.list_b_booster_1[-1][1].grid_forget()
#            self.list_b_booster_1.pop()
            self.list_b_booster_am[-1][1].grid_forget()
#            self.list_b_booster_am.pop()
            # -
#            self.list_var_sum.pop()
            # -
            self.list_fullbelt[-1][1].grid_forget()
#            self.list_fullbelt.pop()
            self.list_buildam[-1][1].grid_forget()
#            self.list_buildam.pop()
            self.linecount -= 1
            self.delete_count += 1
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
         
        
    def del_row_line(self, row):
        print("del_row_line, row", row)
        self.list_del_button[row].grid_forget()
#        self.list_del_button.pop(row)
        # -
#        self.list_dropvar.pop(row)
        self.list_dropmenu[row].grid_forget()
#        self.list_dropmenu.pop(row)
        # -
        self.list_builder[row][1].grid_forget()
#        self.list_builder.pop(row)
        self.list_belt[row][1].grid_forget()
#        self.list_belt.pop(row)
        self.list_ipm_in[row][1].grid_forget()
#        self.list_ipm_in.pop(row)
        self.list_booster_1[row][1].grid_forget()
#        self.list_booster_1.pop(row)
        self.list_booster_2[row][1].grid_forget()
#        self.list_booster_2.pop(row)
        self.list_booster_3[row][1].grid_forget()
#        self.list_booster_3.pop(row)
        self.list_booster_4[row][1].grid_forget()
#        self.list_booster_4.pop(row)
        self.list_b_booster_1[row][1].grid_forget()
#        self.list_b_booster_1.pop(row)
        self.list_b_booster_am[row][1].grid_forget()
#        self.list_b_booster_am.pop(row)
        # -
#        self.list_var_sum.pop(row)
        # -
        self.list_fullbelt[row][1].grid_forget()
#        self.list_fullbelt.pop(row)
        self.list_buildam[row][1].grid_forget()
#        self.list_buildam.pop(row)

        self.linecount -= 1
        self.delete_count += 1



root = tk.Tk()

app = Application(master=root)
app.title = "Factorio Calc"
root.mainloop()

print("mainloop out, Exit")
