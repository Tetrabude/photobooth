import Tkinter

from PIL import ImageTk, Image
from server import flickrConnect as fCon

class gui():
    

    def __init__(self, cam):
        self.cam = cam
        
        self.root = Tkinter.Tk()
        #self.root.overrideredirect(True)
        
        print('Gui initialized')

        self.w, self.h = self.root.winfo_screenwidth()-25, self.root.winfo_screenheight()-25
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
        Tkinter.Label(self.root, image=self.logo).place(x=30, y= self.h - 220)
        
    def loadImage(self):
        self.photoPath = self.cam.takePhoto()
        originalImg = Image.open(self.photoPath)
        (originalImgWidth, originalImgHeight) = originalImg.size
        imgProportion = originalImgWidth / originalImgHeight
    
        imgWidth = self.w - 300 # int(self.w * 0.72)
        imgHeight = self.h - 250 #int(imgWidth / imgProportion)
        
        resizedImg = originalImg.resize((imgWidth , imgHeight),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(resizedImg)
        
        Tkinter.Label(self.root, image = self.img).place(x=5, y=5)
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
        Tkinter.Button(self.root, text="Upload Picture", image=self.deleteIcon).place(x=self.w - 280, y= 630)

    
    def takePicture(self):
        self.loadImage()
        
    def uploadPicture(self):
        fInst = fCon.flickrConnect()
        fInst.upload(self.photoPath)
       

        #panel = Label(root, image = img)
        # panel.pack(side = "bottom", fill = "both", expand = "yes")


