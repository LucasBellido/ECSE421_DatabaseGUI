import tkinter as tk
from tkinter import font as tkfont

from databasequeries import *


class UsersPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        UserTitleLabel = tk.Label(self, text="Users Page",
                                   font=controller.title_font)
        UserTitleLabel.pack(side="top", fill="x", pady=10)
        returnMenubutton = tk.Button(self, text="Return to Main Menu",
                                     command=lambda: controller.show_frame("StartPage"))
        returnMenubutton.pack()

        labelTitle = tk.Label(self, text="(User Email, User Birthday)")
        labelTitle.pack()
        # call getAlbums from databasequeries.py and place them in a scrollable list box
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side="right", fill="y")
        self.listbox = tk.Listbox(self, yscrollcommand=scrollbar.set, width=50)
        self.loadUsers()
        self.listbox.pack(side="left", fill="both")
        scrollbar.config(command=self.listbox.yview)

        # initialize buttons and text
        
        createButton = tk.Button(
            self, text="Create entry", command=lambda: controller.show_frame("CreateUser"))
        createButton.pack()
        # USE "self.label = ..." instead of "label = ..." when initialize the label to be able to access it outside of this function,
        # since label not globally defined so would be out of scope if tried to modify the label in modifyEntry().
        # So by using self, you can modify label in another function without globally defining it.
        self.errorLabel = tk.Label(self, text="", fg="red")
        self.errorLabel.pack()

    def useArgument(self, arg):
        if (arg == "updatePage"):
            self.loadUsers()

    def loadUsers(self):
        self.listbox.delete(0, 'end')
        userList = getUsers()
        for user in userList:
            self.listbox.insert("end", str(user))

    def modifyEntry(self):
        # this checks if an entry is not selected
        if not self.listbox.curselection():
            self.errorLabel['text'] = "Please select an entry"
            self.errorLabel.after(1500, self.on_after)
        # this checks that an entry is selected
        else:
            selectedString = self.listbox.get(self.listbox.curselection())

            userEmail = selectedString.split(',')[0].replace('(', '').replace("'", "").lstrip()

            # pass album id as argument to a new page
            self.controller.show_frame("SpecificUserEntry", userEmail)

    # this method clears the error and gets called after 1500 milliseconds
    def on_after(self):
        self.errorLabel.configure(text="")