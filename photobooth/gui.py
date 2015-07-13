import Tkinter


from PIL import ImageTk, Image
from server.flickr import flickr

class gui():
    

    def __init__(self, cam):
        self.cam = cam
        
        self.root = Tkinter.Tk()
        #self.root.overrideredirect(True)
        
        print('Gui initialized')

        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        #self.w, self.h = 1200, 800
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))
        
        self.loadButtons()
        self.loadLogo()
        self.loadImage()
        
    def run(self):
        self.root.mainloop()
        return 0
        
    def loadLogo(self):
        originalLogo = Image.open("Kontingentsabzeichen.png")
        originalLogo = originalLogo.resize(( 175, 175 ),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(originalLogo)
        Tkinter.Label(self.root, image=self.logo).place(x=self.w - 180, y= self.h - 180)
        
    def loadImage(self):
        self.photoPath = self.cam.takePhoto()
        originalImg = Image.open(self.photoPath)
        (originalImgWidth, originalImgHeight) = originalImg.size
        imgProportion = originalImgWidth / originalImgHeight
    
        imgWidth = self.w - 200 # int(self.w * 0.72)
        imgHeight = self.h - 200 #int(imgWidth / imgProportion)
        
        resizedImg = originalImg.resize((imgWidth , imgHeight),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(resizedImg)
        
        Tkinter.Label(self.root, image = self.img).place(x=5, y=5)
        #img.grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
    
    def loadButtons(self):
    
        Tkinter.Label(self.root, text="Lorem Ipsum").place(x=self.w - 180, y= 10)
        
        Tkinter.Button(self.root, text="Take Picture", command = self.takePicture).place(x= 20, y= self.h-180)
    
        Tkinter.Button(self.root, text="Discard Picture").place(x= 20, y= self.h-140)
    
        Tkinter.Button(self.root, text="Upload Picture", command = self.uploadPicture).place(x= 20, y= self.h-100)

    
    def takePicture(self):
        self.loadImage()
        
    def uploadPicture(self):
        flickr.upload(self.photoPath)
       

        #panel = Label(root, image = img)
        # panel.pack(side = "bottom", fill = "both", expand = "yes")


