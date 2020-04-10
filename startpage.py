import tkinter as tk
from tkinter import font as tkfont


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the Main Menu of Group 24",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        AlbumsPageButton = tk.Button(self, text="View/Edit/Create Albums",
                                     command=lambda: controller.show_frame("AlbumsPage"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        exitButton = tk.Button(self, text="Exit Peacefully",
                               command=lambda: self.quit())
        AlbumsPageButton.pack()
        button2.pack()
        exitButton.pack()
