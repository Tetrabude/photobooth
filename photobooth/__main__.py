

import os
import subprocess
import sys



import gui

try:
    import gphoto2 as gp
    print("gphoto2 loaded")
    import client.camera as camera
except ImportError:
    print("cameraMock loaded")
    import client.cameraMock as camera


def main():
    print('Main rutine started')
    cam = camera.camera()
    g = gui.gui(cam)

    g.run()
    
    
if __name__ == "__main__":
    sys.exit(main())
