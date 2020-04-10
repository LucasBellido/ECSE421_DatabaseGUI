import tkinter as tk
from tkinter import font as tkfont

from startpage import StartPage
from albumspage import AlbumsPage
from pagetwo import PageTwo
from specificalbumentry import SpecificAlbumEntry

from databasequeries import *


# this is the main app class that defines which files will be used. Need to go to each file on its own to see the content


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry("500x500")
        self.title("Group 24 Database GUI")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, AlbumsPage, PageTwo, SpecificAlbumEntry):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name, arg=None):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

        if arg:
            frame.arg = arg
            # or
            frame.useArgument(arg)


if __name__ == "__main__":
    app = App()
    app.mainloop()
