

import os
import subprocess
import sys

# import gphoto2 as gp

from tkinter import *


from PIL import ImageTk, Image

def main():
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
    root.overrideredirect(True)

    
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))

    

    originalImg = Image.open(target)
    (originalImgWidth, originalImgHeight) = originalImg.size
    imgProportion = originalImgWidth / originalImgHeight
    
    imgWidth = int(w * 0.72)
    imgHeight = int(imgWidth / imgProportion)
    
    resizedImg = originalImg.resize((imgWidth , imgHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resizedImg)
    
    Label(root, image = img).grid(row=0, column=0)
    #img.grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
    
    Label(root, text="Lorem Ipsum").grid(row=0, column=1)
    
    Button(root, text="Discard Picture").grid(row=1, column=0, sticky=W+E+N+S)
    
    Button(root, text="Upload Picture").grid(row=2, column=0, sticky=W+E+N+S)
    
    originalLogo = Image.open("Kontingentsabzeichen.png")
    
    
    
    originalLogo = originalLogo.resize(( int(h*0.27), int(h*0.27) ),Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(originalLogo)
    Label(root, image=logo).grid(row=1, column=1, rowspan=2, padx=5, pady=5)

     

    #panel = Label(root, image = img)
    # panel.pack(side = "bottom", fill = "both", expand = "yes")

    root.mainloop()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
