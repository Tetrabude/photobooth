import Tkinter
import os
import time

from PIL import ImageTk, Image, ImageFont, ImageDraw
from shutil import copyfile

class gui():
    

    def __init__(self, cam, uploadDir, uploadPrivDir):
        self.cam = cam
        self.uploadDir = uploadDir
        self.uploadPrivDir = uploadPrivDir
        self.root = Tkinter.Tk()
        #self.root.overrideredirect(True)
        print('Gui initialized')

        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        #self.w, self.h = 1280, 1024 #1024, 768 #800, 600#
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))
        

        self.loadPeter()
        self.loadButtons()
        self.loadLogo()
        self.imgLabel = None
        
        
    def run(self):
        self.root.mainloop()
        return 0
        
    def loadLogo(self):
        originalLogo = Image.open("Kontingentsabzeichen.png")
        originalLogo = originalLogo.resize(( 175, 175 ),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(originalLogo)
        Tkinter.Label(self.root, image=self.logo).place(x=30, y= self.h - 220)
        
    def loadPeter(self):
        peter = Image.open("peter.jpg")
        self.smallPeter = self.resizeImage(peter)
        self.smallPeterLabel = Tkinter.Label(self.root, image=self.smallPeter, font=("Roboto-Regular.ttf",300), foreground="red", text="", compound=Tkinter.CENTER)
        self.smallPeterLabel.place(x=5,y=5)
        
    def loadImage(self):
        
        if not self.imgLabel is None:
            self.imgLabel.destroy()
        
        self.photoPath = self.cam.takePhoto()
        originalImg = Image.open(self.photoPath)
        
        #copyfile(self.photoPath, self.uploadPrivDir + self.getPhotoName())
        
        self.tagImage(originalImg)
        self.photoPathPubl = self.photoPath.split('.')[0] + "-publ.jpg" 
        originalImg.save(self.photoPathPubl)
        self.img2 = self.resizeImage(originalImg)
               
        self.imgLabel = Tkinter.Label(self.root, image = self.img2)
        self.imgLabel.place(x=5, y=5)
        #img.grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
    
    def loadButtons(self):
    
        self.infoLabel = Tkinter.Label(self.root, text="Info", font=("Roboto-Regular.ttf", 60))
        self.infoLabel.place(x = 250, y= self.h - 220)
        
        self.connectionLabel = Tkinter.Label(self.root, text="", font=("Roboto-Regular.ttf", 30))
        self.connectionLabel.place(x = 250, y= self.h - 100)
        
        
        self.cameraIcon = Image.open("icon/Camera.png")
        self.cameraIcon = ImageTk.PhotoImage(self.cameraIcon)
        self.takePictureBtn = Tkinter.Button(self.root, text="Take Picture", image=self.cameraIcon, command = self.takePicture)
        self.takePictureBtn.place(x=self.w - 280, y= 30)
        self.takePictureBtn['state'] = 'normal'
    
    
        self.cloudIcon = Image.open("icon/Upload.png")
        self.cloudIcon = ImageTk.PhotoImage(self.cloudIcon)
        self.discardPictureBtn = Tkinter.Button(self.root, text="Discard Picture",image=self.cloudIcon, command = self.uploadPicture )
        self.discardPictureBtn.place(x=self.w - 280, y= 330)
        self.discardPictureBtn['state'] = 'disabled'
        
        self.deleteIcon = Image.open("icon/Rubbish.png")
        self.deleteIcon = ImageTk.PhotoImage(self.deleteIcon)
        self.uploadPictureBtn = Tkinter.Button(self.root, text="Upload Picture", image=self.deleteIcon, command = self.delPicture)
        self.uploadPictureBtn.place(x=self.w - 280, y= 630)
        self.uploadPictureBtn['state'] = 'disabled'
    
    def takePicture(self):
        if not self.imgLabel is None:
            self.imgLabel.destroy()
           
        self.count(5)
        self.loadImage()
        self.makeDesicionState()
        
    def uploadPicture(self):
        photoName = self.getPhotoName()
        copyfile(self.photoPath, self.uploadPrivDir + "Priv-" + photoName)
        copyfile(self.photoPathPubl, self.uploadDir + photoName)
        self.takePhotoState()

    def delPicture(self):
        self.imgLabel.destroy()
        print('Delete Picture: ')
        self.takePhotoState()
        #os.remove(self.photoPath)    
       
    def getPhotoName(self):
        return time.strftime("%Y-%m-%d--%H-%M-%S") + '--GermanPhotoBooth.jpg'

        #panel = Label(root, image = img)
        # panel.pack(side = "bottom", fill = "both", expand = "yes")

    def takePhotoState(self):
        self.infoLabel['foreground'] = "royal blue"
        self.infoLabel['text'] = "Take a picture!"
        
        self.takePictureBtn['state'] = 'normal'
        self.discardPictureBtn['state'] = 'disabled'
        self.uploadPictureBtn['state'] = 'disabled'
    
    def makeDesicionState(self):
        self.infoLabel['foreground'] = "dark green"
        self.infoLabel['text'] = "Upload or delete?"
        
        self.takePictureBtn['state'] = 'disabled'
        self.discardPictureBtn['state'] = 'normal'
        self.uploadPictureBtn['state'] = 'normal'
        
    def setConnectionStatus(self, status, remainingPics):
        if status:
            self.connectionLabel['foreground'] = "dark green"
            self.connectionLabel['text'] = str(remainingPics) + " picture(s) waiting for upload"
        else:
            self.connectionLabel['foreground'] = "red"
            self.connectionLabel['text'] = "No internet at the moment \n" + str(remainingPics) +" picture(s) will be uploaded later"

    def count(self, sec):
        for i in range(sec,0,-1):
            self.smallPeterLabel['text'] = str(i)
            self.root.update()
            time.sleep(1)
        
        self.smallPeterLabel['text'] = ""
        self.root.update()
        
    def tagImage(self, originalImg):
        print('tag image')
        originalImgWidth, originalImgHeight = originalImg.size
        logoImg = Image.open("Kontingentsabzeichen.png")
        
        img_w, img_h = logoImg.size
        offset = ((originalImgWidth - img_w - 10) , (originalImgHeight - img_h - 10))
        originalImg.paste(logoImg, offset)
        
        font = ImageFont.truetype("Roboto-Regular.ttf",60)
        draw = ImageDraw.Draw(originalImg)
        draw.text((20 , originalImgHeight - 100),"#wsj2015de",(255,255,255),font=font)
        draw = ImageDraw.Draw(originalImg)
        
    def resizeImage(self, originalImg):
        print('resize image')
        originalImgWidth, originalImgHeight = originalImg.size
        imgProportion = float(originalImgWidth) / float(originalImgHeight)
        
        imgWidth = self.w - 300 # int(self.w * 0.72)
        imgHeight = int(float(imgWidth) / float(imgProportion))
        
        if imgHeight > (self.h - 250):
            imgHeight = self.h - 250
            imgWidth = int(float(imgHeight)*float(imgProportion))
        
        resizedImg = originalImg.resize((imgWidth , imgHeight),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resizedImg)
        return img
        