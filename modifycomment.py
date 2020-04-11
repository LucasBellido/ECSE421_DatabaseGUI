import tkinter as tk
from tkinter import font as tkfont

from databasequeries import *


class ModifyComment(tk.Frame):

    globalMemoryID = -1
    globaOriginalCommentText = ''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.specificidlabel = tk.Label(self, text="Specific Comments",
                                        font=controller.title_font)
        self.specificidlabel.pack(side="top", fill="x", pady=10)

        # Create Text Box Labels
        self.commentLabel = tk.Label(self, text="Comment")
        self.commentLikesLabel = tk.Label(self, text="Likes")
        # Create Text Boxes
        self.commentText = tk.Entry(self, width=30)
        self.likesText = tk.Entry(self, width=30)

        self.commentLabel.pack(fill="x")
        self.commentText.pack(fill="x")
        self.commentLikesLabel.pack(fill="x")
        self.likesText.pack(fill="x")

        modifybutton = tk.Button(
            self, text="Modify Entry", command=lambda: self.modifyComment())
        modifybutton.pack()

        goBackbutton = tk.Button(self, text="Return to Comments",
                                 command=lambda: self.controller.show_frame("MemoryComments"))
        goBackbutton.pack()

    def useArgument(self, commentArr):
        memoryID = commentArr[0]
        commentText = commentArr[1]

        print(memoryID)
        print(commentText)

        comment = getComment(memoryID, commentText)
        self.globalMemoryID = memoryID
        self.globaOriginalCommentText = commentText

        self.specificidlabel['text'] = "Specific Memory Entry ID: {}".format(
            str(memoryID))
        print(comment)
        # clear comment name box and set new text
        self.commentText.delete(0, tk.END)
        self.commentText.insert(tk.END, comment[1])
        self.likesText.delete(0, tk.END)
        self.likesText.insert(tk.END, comment[2])

    def modifyComment(self):
        modifyCommentEntry(self.globalMemoryID,
                           self.globaOriginalCommentText, self.commentText.get(), self.likesText.get())
        # navigate to the albums page and refresh the table to show the modified one too!!!
        # i place an arg called updatePage which tells the albumspage to do this via the useArgument function
        self.controller.show_frame("MemoryComments", self.globalMemoryID)
