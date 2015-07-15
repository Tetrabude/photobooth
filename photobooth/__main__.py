

import os
import subprocess
import sys



from gui import gui
from server.uploader import uploaderThread

try:
    import gphoto2 as gp
    print("gphoto2 loaded")
    from client.camera import camera as camera

except ImportError:
    print("cameraMock loaded")
    from client.cameraMock import cameraMock as camera



def main():
    print('Main rutine started')
    dir = os.path.dirname(os.path.abspath(__file__))
    print(dir)
    dir = os.path.abspath(dir + '/../')
    print(dir)
    uploadDir = (dir +'/uploadPictures/')
    
    cam = camera()
    g = gui(cam,uploadDir)
    
    deamon = uploaderThread(uploadDir)
    deamon.start()
    g.run()
    deamon.stop()
    deamon.join()
    

    
if __name__ == "__main__":
    sys.exit(main())
