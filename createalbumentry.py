import tkinter as tk
from tkinter import font as tkfont

from databasequeries import *


class CreateAlbumEntry(tk.Frame):

    def __init__(self, parent, controller, attr=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.specificidlabel = tk.Label(self, text="Create Album Entry",
                                        font=controller.title_font)
        self.specificidlabel.pack(side="top", fill="x", pady=10)

        # Create Text Box Labels
        self.albumIDlabel = tk.Label(self, text="Album ID")
        self.albumnamelabel = tk.Label(self, text="Album Name")
        # Create Text Boxes
        self.albumIDText = tk.Entry(self, width=30)
        self.albumnametext = tk.Entry(self, width=30)

        self.albumIDlabel.pack(fill="x")
        self.albumIDText.pack(fill="x")
        self.albumnamelabel.pack(fill="x")
        self.albumnametext.pack(fill="x")

        createbutton = tk.Button(
            self, text="Create Entry", command=lambda: self.createAlbum())
        createbutton.pack()
        goBackbutton = tk.Button(self, text="Return to Album Entries",
                                 command=lambda: self.controller.show_frame("AlbumsPage"))
        goBackbutton.pack()

    def createAlbum(self):
        createAlbumEntry(self.albumIDText.get(),
                         self.albumnametext.get())
        self.controller.show_frame("AlbumsPage", "updatePage")
