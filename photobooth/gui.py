from tkinter import *


from PIL import ImageTk, Image
from photobooth.server.flickr import flickr

class gui():
    

    def __init__(self, cam):
        self.cam = cam
        
        self.root = Tk()
        self.root.overrideredirect(True)
        
        print('Gui initialized')

        #self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.w, self.h = 1200, 800
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))
        
        self.loadButtons()
        self.loadLogo()
        self.loadImage()
        
    def run(self):
        self.root.mainloop()
        return 0
        
    def loadLogo(self):
        originalLogo = Image.open("Kontingentsabzeichen.png")
        originalLogo = originalLogo.resize(( int(self.h*0.27), int(self.h*0.27) ),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(originalLogo)
        Label(self.root, image=self.logo).grid(row=1, column=1, rowspan=3, padx=5, pady=5)
        
    def loadImage(self):
        self.photoPath = self.cam.takePhoto()
        originalImg = Image.open(self.photoPath)
        (originalImgWidth, originalImgHeight) = originalImg.size
        imgProportion = originalImgWidth / originalImgHeight
    
        imgWidth = int(self.w * 0.72)
        imgHeight = int(imgWidth / imgProportion)
        
        resizedImg = originalImg.resize((imgWidth , imgHeight),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(resizedImg)
        
        Label(self.root, image = self.img).grid(row=0, column=0)
        #img.grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
    
    def loadButtons(self):
    
        Label(self.root, text="Lorem Ipsum").grid(row=0, column=1)
        
        Button(self.root, text="Take Picture", command = self.takePicture).grid(row=1, column=0, sticky=W+E+N+S)
    
        Button(self.root, text="Discard Picture").grid(row=3, column=0, sticky=W+E+N+S)
    
        Button(self.root, text="Upload Picture", command = self.uploadPicture).grid(row=2, column=0, sticky=W+E+N+S)

    
    def takePicture(self):
        self.loadImage()
        
    def uploadPicture(self):
        flickr.upload(self.photoPath)
       

        #panel = Label(root, image = img)
        # panel.pack(side = "bottom", fill = "both", expand = "yes")


