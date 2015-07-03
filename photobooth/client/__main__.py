

import os
import subprocess
import sys

import gphoto2 as gp

from tkinter import *
from PIL import ImageTk, Image

def main():
    
    os.system("bash -c \"gvfs-mount -s gphoto2\"")
    
    context = gp.gp_context_new()
    camera = gp.check_result(gp.gp_camera_new())
    gp.check_result(gp.gp_camera_init(camera, context))
 
    print('Capturing image')
    
    file_path = gp.check_result(gp.gp_camera_capture(
        camera, gp.GP_CAPTURE_IMAGE, context))
    
    print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
    
    target = os.path.join('/tmp', file_path.name)
    
    print('Copying image to', target)
    
    camera_file = gp.check_result(gp.gp_camera_file_get(
            camera, file_path.folder, file_path.name,
            gp.GP_FILE_TYPE_NORMAL, context))
    
    gp.check_result(gp.gp_file_save(camera_file, target))
    
    gp.check_result(gp.gp_camera_exit(camera, context))
    
    print('Open image in gui')
    
    root = Tk()
    #root.overrideredirect(True)

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))

    originalImg = Image.open(target)
    resizedImg = originalImg.resize((w, h),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resizedImg)

    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    root.mainloop()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
