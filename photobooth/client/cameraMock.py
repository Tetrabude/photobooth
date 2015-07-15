class cameraMock():
    lastPic = "bild.jpg"
    
    def __init__(self):
        print('CameraMock initialized')
    
    def getPhotoPath(self):
        return "test01.jpg"
    
    def takePhoto(self):
        print('new photo mock')
        if self.lastPic == "test01.jpg" :
            self.lastPic ="test02.jpg"
        else :
            self.lastPic = "test01.jpg"
            
        return self.lastPic