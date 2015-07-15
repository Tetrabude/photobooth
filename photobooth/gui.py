import Tkinter
import os
import time

from PIL import ImageTk, Image
from server import flickrConnect as fCon
from shutil import copyfile

class gui():
    

    def __init__(self, cam, uploadDir):
        self.cam = cam
        self.uploadDir = uploadDir
        self.root = Tkinter.Tk()
        #self.root.overrideredirect(True)
        
        print('Gui initialized')

        #self.w, self.h = self.root.winfo_screenwidth()-25, self.root.winfo_screenheight()-25
        self.w, self.h = 1280, 1024 #1024, 768 #800, 600#
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))
        
        self.loadButtons()
        self.loadLogo()
        
        
    def run(self):
        self.root.mainloop()
        return 0
        
    def loadLogo(self):
        originalLogo = Image.open("Kontingentsabzeichen.png")
        originalLogo = originalLogo.resize(( 175, 175 ),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(originalLogo)
        Tkinter.Label(self.root, image=self.logo).place(x=30, y= self.h - 220)
        
    def loadImage(self):
        self.photoPath = self.cam.takePhoto()
        originalImg = Image.open(self.photoPath)
        (originalImgWidth, originalImgHeight) = originalImg.size
        
        imgProportion = float(originalImgWidth) / float(originalImgHeight)
        
        imgWidth = self.w - 300 # int(self.w * 0.72)
        imgHeight = int(float(imgWidth) / float(imgProportion))
        
        if imgHeight > (self.h - 250):
            imgHeight = self.h - 250
            imgWidth = int(float(imgHeight)*float(imgProportion))
        
        resizedImg = originalImg.resize((imgWidth , imgHeight),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(resizedImg)
               
        self.imgLabel = Tkinter.Label(self.root, image = self.img)
        self.imgLabel.place(x=5, y=5)
        #img.grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
    
    def loadButtons(self):
    
        Tkinter.Label(self.root, text="Lorem Ipsum").place(x = 250, y= self.h - 220)
        
        
        self.cameraIcon = Image.open("icon/Camera.png")
        self.cameraIcon = ImageTk.PhotoImage(self.cameraIcon)
        Tkinter.Button(self.root, text="Take Picture", image=self.cameraIcon, command = self.takePicture).place(x=self.w - 280, y= 30)
    
        self.cloudIcon = Image.open("icon/Upload.png")
        self.cloudIcon = ImageTk.PhotoImage(self.cloudIcon)
        Tkinter.Button(self.root, text="Discard Picture",image=self.cloudIcon, command = self.uploadPicture ).place(x=self.w - 280, y= 330)
    
        self.deleteIcon = Image.open("icon/Rubbish.png")
        self.deleteIcon = ImageTk.PhotoImage(self.deleteIcon)
        Tkinter.Button(self.root, text="Upload Picture", image=self.deleteIcon, command = self.delPicture).place(x=self.w - 280, y= 630)

    
    def takePicture(self):
        self.imgLabel.destroy()
        self.loadImage()
        
    def uploadPicture(self):
        copyfile(self.photoPath, self.uploadDir + self.getPhotoName())

    def delPicture(self):
        self.imgLabel.destroy()
        print('Delete Picture: ')
        #os.remove(self.photoPath)    
       
    def getPhotoName(self):
        return time.strftime("%Y-%m-%d--%H-%M-%S") + '--GermanPhotoBooth.jpg'

        #panel = Label(root, image = img)
        # panel.pack(side = "bottom", fill = "both", expand = "yes")

    def takePhotoState(self):
        pass
    
    def makeDesicionState(self):
        pass
