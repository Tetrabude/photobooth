'''
Created on 19.06.2015

@author: peter
'''

from tkinter import *
from PIL import ImageTk, Image
import os


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


root = Tk()
root.title("Arthur rennt durchs Bild")
img = ImageTk.PhotoImage(Image.open("test-kl.jpg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

app=FullScreenApp(root)

root.mainloop()







