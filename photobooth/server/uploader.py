'''
Created on 13.07.2015

@author: peter
'''

import time
import os
import flickrConnect as fCon
import threading
import xml.etree

class uploaderThread(threading.Thread):
    
    def __init__(self, path, g):
        print('initialize uploader')
        threading.Thread.__init__(self)
        self.path = path
        self.gui = g
        
        super (uploaderThread, self).__init__()
        self._stop_req = threading.Event()
        
        
    def upload(self):
        path = os.listdir(self.path)
                
        for picture in path:
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
                        self.gui.setConnectionStatus(True, len(os.listdir(self.path)))
                    else:
                        self.gui.setConnectionStatus(False, len(os.listdir(self.path))) 
                    
                except Exception as e:
                    print('Upload Failed: ')
                    print(e)
                    self.gui.setConnectionStatus(False, len(os.listdir(self.path)))
                    
        
    def run(self):
        while not self._stop_req.isSet():
            print('Deamon is looking for new pictures')
            self.upload()
            time.sleep(5)
    
    def stop(self):
        self._stop_req.set();