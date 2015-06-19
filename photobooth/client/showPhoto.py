'''
Created on 19.06.2015

@author: peter
'''

from tkinter import *
from PIL import ImageTk, Image

def showPhoto(path):

    
    root = Tk()
    #root.overrideredirect(True)

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))

    originalImg = Image.open(path)
    resizedImg = originalImg.resize((w, h),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resizedImg)

    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    root.mainloop()










