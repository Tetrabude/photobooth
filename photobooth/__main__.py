

import os
import subprocess
import sys




from photobooth.gui import gui

try:
    import gphoto2 as gp
    print("gphoto2 loaded")
    from photobooth.client.camera import camera as camera
except ImportError:
    print("cameraMock loaded")
    from photobooth.client.cameraMock import cameraMock as camera


def main():
    print('Main rutine started')
    cam = camera()
    g = gui(cam)

    g.run()
    
    
if __name__ == "__main__":
    sys.exit(main())
