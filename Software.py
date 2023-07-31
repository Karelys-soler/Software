
# User Interface
import tkinter as tk
import re

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Menu import menu
from os import system

class Form:
    def Register():
        try:
            root = tk.Tk()
            root.title("Python")
            root.geometry("1050x550")
            menu(root)



            #Theme
            style = ttk.Style(root)
            root.tk.call("source", "forest-light.tcl")
            root.tk.call("source", "forest-dark.tcl")
            style.theme_use("forest-dark")
            

            #Mode Function
            def modeFunction():
                if mode.instate(["selected"]):
                    style.theme_use("forest-light")
                    root.config(bg='#ffffff')
                    groupbox.config(bg="#ffffff")
                    groupbox.config(fg="#313131")
                    tree.config(bg="#ffffff")
                    tree.config(fg="#313131")

                else:
                    style.theme_use("forest-dark")
                    root.config(bg="#313131")
                    groupbox.config(bg="#313131")
                    groupbox.config(fg="#ffffff")
                    tree.config(bg="#313131")
                    tree.config(fg="#ffffff")


            #SAVE
            def insert():
                #Name
                name = label.get()
                patrom1 = r"^[A-Z][a-z]+$"
                coincidencia = re.match(patrom1, name)
                if coincidencia:
                    print("Coincidencia encontrada")
                else:
                    print("Coincidencia no encontrada")
                #Last Name
                lastname = labelLastName.get()
                patrom2 = r"^[A-Z][a-z]+$"
                coincidencialastname = re.match(patrom2, lastname)
                if coincidencialastname:
                    print("Coincidencia encontrada")
                else:
                    print("Coincidencia no encontrada")
                #Age
                age = (selectedAge.get())
                patrom3 = r"^(1[89]|[2-9][0-9]|100)$"
                coincidenciaAge = re.match(patrom3, age)
                if coincidenciaAge:
                    print("Coincidencia encontrada")
                else:
                    print("Coincidencia no encontrada")
                #Gender
                gender = combobox.get()
                patrom4 = r"^[A-Z][a-z]+$"
                coincidenciagender = re.match(patrom4, gender)
                if coincidenciagender:
                    print("Coincidencia encontrada")
                else:
                    print("Coincidencia no encontrada")
                #Country
                country = comboboxx.get()
                patrom5= r"^[A-Z][a-z]+$"
                coincidenciacountry = re.match(patrom5, country)
                if coincidenciacountry:
                    print("Coincidencia encontrada")
                else:
                    print("Coincidencia no encontrada")
                #Number
                number = labelNumber.get()
                patrom6 = r"^\d{10}$"
                coincidenciaNumber = re.match(patrom6, number)
                if coincidenciaNumber:
                    print("Coincidencia encontrada")
                else:
                    print("Coincidencia no encontrada")
                #Email
                email = labelEmail.get()
                patrom7 = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                coincidenciaEmail = re.match(patrom7, email)
                if coincidenciaEmail:
                    print("Coincidencia encontrada")
                else:
                    print("Coincidencia no encontrada")
                #Agree
                agree = "Agree" if var.get() else "Disagree"

                #Message
                print(f"Se registro el usuario: {name} {lastname}, de {age} años de edad, residenciado en {country} y titular del correo: {email} / {agree} / Software de {name} {lastname}")

                #View Users
                treeView.insert('', tk.END, values=(name, lastname, age, gender, country, number, email, agree))


                #CLEAR FORM
                #Name
                label.delete(0, "end")
                label.insert(0, "Name")
                #Last Name
                labelLastName.delete(0, "end")
                labelLastName.insert(0, "Last Name")
                #Age
                selectedAge.delete(0, "end")
                selectedAge.insert(0, "Age")
                #Gender
                combobox.delete(0, "end")
                combobox.insert(0, "Gender")
                #Country
                comboboxx.delete(0, "end")
                comboboxx.insert(0, "Country")
                #Number
                labelNumber.delete(0, "end")
                labelNumber.insert(0, "Number")
                #Email
                labelEmail.delete(0, "end")
                labelEmail.insert(0, "Email")
                #Check
                checkbox.state(["!selected"])

            #EDIT
            #DELETE

            #Register
            groupbox = LabelFrame(root, text="Register", padx=5, pady=5)
            groupbox.grid(row=0, column=0, padx=10, pady=10)

            #Label Name
            label = ttk.Entry(groupbox)
            label.insert(0, "Name")
            label.bind("<FocusIn>", lambda event: label.delete("0", "end"))
            label.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")

            #label Last Name
            labelLastName = ttk.Entry(groupbox)
            labelLastName.insert(0, "Last Name")
            labelLastName.bind("<FocusIn>", lambda event: labelLastName.delete("0", "end"))
            labelLastName.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

            #label Age
            selectedAge = ttk.Spinbox(groupbox, from_=18, to=100, cursor="hand2")
            selectedAge.insert(0, "Age")
            selectedAge.grid( row=2, column=0, padx=5, pady=5, sticky="ew")

            #label Gender
            selectedGender = ttk.Scrollbar(groupbox)
            genderList = ("Male", "Female", "Other")
            combobox = ttk.Combobox(groupbox, values= genderList, cursor="hand2", textvariable=selectedGender)
            combobox.insert(0, "Gender")
            combobox.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

            #label Country
            selectedCountry = ttk.Scrollbar(groupbox)
            list = ("Argentina", "Bolivia", "Brazil", "Canada", "Colombia", "Costa Rica","Chile", "Dominican Republic", "Ecuador", "France", "Greece", "Guatemala","Honduras","Italia","Mexico","Uruguay","USA","Venezuela","Other")
            comboboxx = ttk.Combobox(groupbox, values= list, cursor="hand2", textvariable=selectedCountry)
            comboboxx.insert(0, "Country")
            comboboxx.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

            #label Number
            labelNumber= ttk.Entry(groupbox)
            labelNumber.insert(0, "Number")
            labelNumber.bind("<FocusIn>", lambda event: labelNumber.delete("0", "end"))
            labelNumber.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

            #label Email
            labelEmail= ttk.Entry(groupbox)
            labelEmail.insert(0, "Email")
            labelEmail.bind("<FocusIn>", lambda event: labelEmail.delete("0", "end"))
            labelEmail.grid(row=6, column=0, padx=5, pady=5, sticky="ew")



            #Checkbox
            var = BooleanVar(groupbox)
            checkbox = ttk.Checkbutton(groupbox, text="Agree",cursor="hand2", variable=var)
            checkbox.grid(row=7, column=0, padx=5, pady=5, sticky="ew")


            #Buttons

            #Button Save
            buttonSave = ttk.Button(groupbox, text="Save", width=10, cursor="hand2", command= insert)
            buttonSave.grid(row=8, column=0, padx=5, pady=5, sticky="nsew")

            #Button Edit
            buttonEdit = ttk.Button(groupbox, text="Edit", width=10, cursor="hand2")
            buttonEdit.grid(row=9, column=0, padx=5, pady=5, sticky="nsew")

            #Button Delete
            buttonDelete = ttk.Button(groupbox, text="Delete", cursor="hand2", width=10)
            buttonDelete.grid(row=10, column=0, padx=5, pady=5, sticky="nsew")



            #Separator
            separator = ttk.Separator(groupbox)
            separator.grid(row=11, column=0, padx=5, pady=5, sticky="ew")



            #Switch
            mode = ttk.Checkbutton(groupbox, text="Mode", style="Switch", cursor="hand2", command=modeFunction)
            mode.grid(row=12, column=0, padx=5, pady=10, sticky="nsew")



            #Users List
            tree = LabelFrame(root, text="Users List", padx=5, pady=5, )
            tree.grid(row=0, column=1, padx=10, pady=10)

            #Columns
            treeScroll = ttk.Scrollbar(tree)
            treeScroll.pack(side="right", fill="y")
            
            cols = ("First Name", "Last Name", "Age", "Gender","Country", "Number", "Email")
            treeView = ttk.Treeview(tree, columns=cols, show="headings", yscrollcommand=treeScroll.set, height=22)

            #First Name
            treeView.column("#1", anchor=CENTER, width=100)
            treeView.heading ("#1", text="First Name")

            #Last Name
            treeView.column("#2", anchor=CENTER, width=100)
            treeView.heading ("#2", text="Last Name")

            #Age
            treeView.column("#3", anchor=CENTER, width=50)
            treeView.heading ("#3", text="Age")

            #Gender
            treeView.column("#4", anchor=CENTER, width=100)
            treeView.heading ("#4", text="Gender")

            #Country
            treeView.column("#5", anchor=CENTER, width=100)
            treeView.heading ("#5", text="Country")

            #Number
            treeView.column("#6", anchor=CENTER, width=100)
            treeView.heading ("#6", text="Number")

            #Email
            treeView.column("#7", anchor=CENTER, width=150)
            treeView.heading ("#7", text="Email")



            treeView.pack()
            treeScroll.config(command=treeView.yview)
            root.mainloop()
        except: 
            print("Error")

    Register()
    