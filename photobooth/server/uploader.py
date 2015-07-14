'''
Created on 13.07.2015

@author: peter
'''

import time
import os
import flickrConnect as fCon
import threading

class uploaderThread(threading.Thread):
    
    def __init__(self, path):
        print('initialize uploader')
        threading.Thread.__init__(self)
        self.path = path
        
        super (uploaderThread, self).__init__()
        self._stop_req = threading.Event()
        
        
    def upload(self):
        for picture in os.listdir(self.path):
            if picture.endswith(".jpg"):
                print('Upload: ' + picture)
                fInst = fCon.flickrConnect()
                fInst.upload(self.path + picture)
        
    def run(self):
        while not self._stop_req.isSet():
            print('Deamon is looking for new pictures')
            self.upload()
            time.sleep(5)
    
    def stop(self):
        self._stop_req.set();