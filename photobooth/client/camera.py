'''
Created on 19.06.2015

@author: peter
'''

import os

try:
    import gphoto2 as gp
    print("gphoto2 loaded")
except ImportError: 
    print("Camera could not be imported")
    
    
class camera():
    
    def __init__(self):
        print('Camera initialized')
    
    def takePhoto(self):
    
        context = gp.gp_context_new()
        camera = gp.check_result(gp.gp_camera_new())
        gp.check_result(gp.gp_camera_init(camera, context))
 
        print('Capturing image')
    
        file_path = gp.check_result(gp.gp_camera_capture(camera, gp.GP_CAPTURE_IMAGE, context))
    
        print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
    
        gp.get
    
        target = os.path.join('/tmp', file_path.name)
    
        print('Copying image to', target)
    
        camera_file = gp.check_result(gp.gp_camera_file_get(
            camera, file_path.folder, file_path.name,
            gp.GP_FILE_TYPE_NORMAL, context))
    
        gp.check_result(gp.gp_file_save(camera_file, target))
    
        gp.check_result(gp.gp_camera_exit(camera, context))  
    
        return target









