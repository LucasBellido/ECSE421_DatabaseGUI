import tkinter as tk
from tkinter import font as tkfont

from databasequeries import *


class CreateUser(tk.Frame):

    def __init__(self, parent, controller, attr=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.specificidlabel = tk.Label(self, text="Create New User",
                                        font=controller.title_font)
        self.specificidlabel.pack(side="top", fill="x", pady=10)

        # Create Text Box Labels
        self.useremaillabel = tk.Label(self, text="User Email")
        self.firstnamelabel = tk.Label(self, text="First Name")
        self.lastnamelabel = tk.Label(self, text="Last Name")
        self.bdaylabel = tk.Label(self, text="Birthday")
        self.addresslabel = tk.Label(self, text="Address")
        self.desclabel = tk.Label(self, text="Description")
        self.picutrelabel = tk.Label(self, text="Picture")

        # Create Text Boxes
        self.useremailtext = tk.Entry(self, width=30)
        self.firstnametext = tk.Entry(self, width=30)
        self.lastnametext = tk.Entry(self, width=30)
        self.bdaytext = tk.Entry(self, width=30)
        self.addresstext = tk.Entry(self, width=30)
        self.desctext = tk.Entry(self, width=30)
        self.picutretext = tk.Entry(self, width=30)


        self.useremaillabel.pack(fill="x")
        self.useremailtext.pack(fill="x")
        self.firstnamelabel.pack(fill="x")
        self.firstnametext.pack(fill="x")
        self.lastnamelabel.pack(fill="x")
        self.lastnametext.pack(fill="x")
        self.bdaylabel.pack(fill="x")
        self.bdaytext.pack(fill="x")
        self.addresslabel.pack(fill="x")
        self.addresstext.pack(fill="x")
        self.desclabel.pack(fill="x")
        self.desctext.pack(fill="x")
        self.picutrelabel.pack(fill="x")
        self.picutretext.pack(fill="x")

        createbutton = tk.Button(
            self, text="Create Entry", command=lambda: self.createUser())
        createbutton.pack()
        goBackbutton = tk.Button(self, text="Return to User Entries",
                                 command=lambda: self.controller.show_frame("UsersPage"))
        goBackbutton.pack()

    def createUser(self):
        error = createUserEntry(self.useremailtext.get(), self.firstnametext.get(), self.lastnametext.get(), self.bdaytext.get(), self.addresstext.get(), self.desctext.get(), self.picutretext.get())
        if not error:
            self.controller.show_frame("UsersPage", "updatePage")