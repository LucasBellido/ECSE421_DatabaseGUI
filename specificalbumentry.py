import tkinter as tk
from tkinter import font as tkfont

from databasequeries import *


class SpecificAlbumEntry(tk.Frame):

    globalAlbumID = -1

    def __init__(self, parent, controller, attr=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.specificidlabel = tk.Label(self, text="Specific Album Entry",
                                        font=controller.title_font)
        self.specificidlabel.pack(side="top", fill="x", pady=10)

        # Create Text Box Labels
        self.albumnamelabel = tk.Label(self, text="Album Name")
        # Create Text Boxes
        self.albumnametext = tk.Entry(self, width=30)

        self.albumnamelabel.pack(fill="x")
        self.albumnametext.pack(fill="x")

        modifybutton = tk.Button(
            self, text="Modify Entry", command=lambda: self.modifyAlbum())
        modifybutton.pack()
        goBackbutton = tk.Button(self, text="Return to Album Entries",
                                 command=lambda: self.controller.show_frame("AlbumsPage"))
        goBackbutton.pack()

    def useArgument(self, albumID):
        album = getAlbum(albumID)
        self.globalAlbumID = albumID

        self.specificidlabel['text'] = "Specific Album Entry ID: {}".format(
            str(albumID))

        # clear album name box and set new text
        self.albumnametext.delete(0, tk.END)
        self.albumnametext.insert(tk.END, album[1])

    def modifyAlbum(self):
        modifyAlbumEntry(self.globalAlbumID,
                         self.albumnametext.get())
        # navigate to the albums page and refresh the table to show the modified one too!!!
        # i place an arg called updatePage which tells the albumspage to do this via the useArgument function
        self.controller.show_frame("AlbumsPage", "updatePage")
