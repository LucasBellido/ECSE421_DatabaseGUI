import tkinter as tk
from tkinter import font as tkfont

from databasequeries import *


class AlbumsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        AlbumTitleLabel = tk.Label(self, text="Albums Page",
                                   font=controller.title_font)
        AlbumTitleLabel.pack(side="top", fill="x", pady=10)
        returnMenubutton = tk.Button(self, text="Return to Main Menu",
                                     command=lambda: controller.show_frame("StartPage"))
        returnMenubutton.pack()

        labelTitle = tk.Label(self, text="(Album ID, Album Name)")
        labelTitle.pack()
        # call getAlbums from databasequeries.py and place them in a scrollable list box
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side="right", fill="y")
        self.listbox = tk.Listbox(self, yscrollcommand=scrollbar.set, width=50)
        self.loadAlbums()
        self.listbox.pack(side="left", fill="both")
        scrollbar.config(command=self.listbox.yview)

        # initialize buttons and text
        modifyButton = tk.Button(
            self, text="Modify entry", command=lambda: self.modifyEntry())
        modifyButton.pack()
        createButton = tk.Button(
            self, text="Create entry", command=lambda: controller.show_frame("CreateAlbumEntry"))
        createButton.pack()
        # USE "self.label = ..." instead of "label = ..." when initialize the label to be able to access it outside of this function,
        # since label not globally defined so would be out of scope if tried to modify the label in modifyEntry().
        # So by using self, you can modify label in another function without globally defining it.
        self.errorLabel = tk.Label(self, text="", fg="red")
        self.errorLabel.pack()

    def useArgument(self, arg):
        if arg == "updatePage":
            self.loadAlbums()

    def loadAlbums(self):
        self.listbox.delete(0, 'end')
        albumList = getAlbums()
        for album in albumList:
            self.listbox.insert("end", str(album))

    def modifyEntry(self):
        # this checks if an entry is not selected
        if not self.listbox.curselection():
            self.errorLabel['text'] = "Please select an entry"
            self.errorLabel.after(1500, self.on_after)
        # this checks that an entry is selected
        else:
            selectedString = self.listbox.get(self.listbox.curselection())

            albumID = selectedString.split(',')[0].replace(
                '(', '').replace("'", "").lstrip()

            # pass album id as argument to a new page
            self.controller.show_frame("SpecificAlbumEntry", albumID)

    # this method clears the error and gets called after 1500 milliseconds
    def on_after(self):
        self.errorLabel.configure(text="")
