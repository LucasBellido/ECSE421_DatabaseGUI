import tkinter as tk
from tkinter import font as tkfont

from databasequeries import *


class MemoryComments(tk.Frame):

    globalMemoryID = -1

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.specificidlabel = tk.Label(self, text="Specific Comments",
                                        font=controller.title_font)
        self.specificidlabel.pack(side="top", fill="x", pady=10)

        labelTitle = tk.Label(
            self, text="(MemoryID, Comment, Likes)")
        labelTitle.pack()
        # call getAlbums from databasequeries.py and place them in a scrollable list box
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side="right", fill="y")
        self.listbox = tk.Listbox(
            self, yscrollcommand=scrollbar.set, width=50)
        self.listbox.pack(side="left", fill="both")
        scrollbar.config(command=self.listbox.yview)

        modifyButton = tk.Button(
            self, text="Modify Comment", command=lambda: self.modifyEntry())
        modifyButton.pack()
        # initialize buttons and text

        goBackbutton = tk.Button(self, text="Return to Memory Entries",
                                 command=lambda: self.controller.show_frame("MemoriesPage"))
        goBackbutton.pack()
        self.errorLabel = tk.Label(self, text="", fg="red")
        self.errorLabel.pack()

    def useArgument(self, memoryID):
        commentList = getMemoryComments(memoryID)
        self.globalMemoryID = memoryID

        self.specificidlabel['text'] = "Specific Comments for Memory Entry ID: {}".format(
            str(memoryID))

        self.listbox.delete(0, 'end')
        for comment in commentList:
            self.listbox.insert("end", str(comment))

    def modifyEntry(self):
        # this checks if an entry is not selected
        if not self.listbox.curselection():
            self.errorLabel['text'] = "Please select an entry"
            self.errorLabel.after(1500, self.on_after)
        # this checks that an entry is selected
        else:
            selectedString = self.listbox.get(self.listbox.curselection())

            memoryID = selectedString.split(',')[0].replace(
                '(', '').replace("'", "").lstrip()

            memoryText = selectedString.split(',')[1].replace(
                '(', '').replace("'", "").lstrip()

            # pass album id as argument to a new page
            self.controller.show_frame("ModifyComment", [memoryID, memoryText])

    # this method clears the error and gets called after 1500 milliseconds
    def on_after(self):
        self.errorLabel.configure(text="")
