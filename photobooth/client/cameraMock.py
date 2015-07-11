class cameraMock():
    
    def __init__(self):
        print('Camera initialized')
    
    def getPhotoPath(self):
        return "test.jpg"
    
    def takePhoto(self):
        return "test.jpg"