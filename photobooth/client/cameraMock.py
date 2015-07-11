class cameraMock():
    lastPic = "bild.jpg"
    
    def __init__(self):
        print('CameraMock initialized')
    
    def getPhotoPath(self):
        return "test.jpg"
    
    def takePhoto(self):
        
        if self.lastPic == "test.jpg" :
            self.lastPic ="bild.jpg"
        else :
            self.lastPic = "test.jpg"
            
        return self.lastPic