

import os
import subprocess
import sys




from photobooth.gui import gui
from photobooth.client.camera import camera


def main():
    print('Main rutine started')
    cam = camera()
    g = gui(cam)

    g.run()
    
    
if __name__ == "__main__":
    sys.exit(main())
