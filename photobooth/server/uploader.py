'''
Created on 13.07.2015

@author: peter
'''

import time
import os
import flickrConnect as fCon
import threading
from pip._vendor.requests.exceptions import ConnectionError
from requests.exceptions import ConnectionError

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
                              
                try: 
                    fInst = fCon.flickrConnect()
                    resp = fInst.upload(self.path + picture)
                    print(resp)
                    print('Remove:' + picture)
                    os.remove(self.path + picture)
                
                except ConnectionError as e:
                    print(e)
        
    def run(self):
        while not self._stop_req.isSet():
            print('Deamon is looking for new pictures')
            self.upload()
            time.sleep(5)
    
    def stop(self):
        self._stop_req.set();