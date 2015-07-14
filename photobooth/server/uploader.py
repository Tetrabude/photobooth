'''
Created on 13.07.2015

@author: peter
'''

import time
import os
import flickrConnect as fCon
import threading
from pip._vendor.requests.exceptions import ConnectionError
import xml.etree

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
                   
                    if resp is not None:
                        print('Respond:')
                        xml.etree.ElementTree.dump(resp)
                        
                        print('Remove:' + picture)
                        os.remove(self.path + picture)
                
                except Exception as e:
                    print('Upload Failed: ')
                    print(e)
                    
        
    def run(self):
        while not self._stop_req.isSet():
            print('Deamon is looking for new pictures')
            self.upload()
            time.sleep(5)
    
    def stop(self):
        self._stop_req.set();