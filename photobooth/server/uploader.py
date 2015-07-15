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
    
    def __init__(self, path, privpath, g):
        print('initialize uploader')
        threading.Thread.__init__(self)
        self.path = path
        self.privpath = privpath
        self.gui = g
        
        super (uploaderThread, self).__init__()
        self._stop_req = threading.Event()
        
        
    def upload(self, dir, publ):
        path = os.listdir(dir)
                
        for picture in path:
            if picture.endswith(".jpg"):
                print('Upload: ' + picture)
                              
                try: 
                    filename = str(dir + picture)
                    fInst = fCon.flickrConnect()
                    resp = fInst.upload(filename,publ)
                   
                    if resp is not None: 
                        print('Respond:')
                        xml.etree.ElementTree.dump(resp)
                        
                        print('Remove:' + picture)
                        os.remove(dir + picture) 
                        self.gui.setConnectionStatus(True, len(os.listdir(dir)))
                    else:
                        self.gui.setConnectionStatus(False, len(os.listdir(dir))) 
                    
                except Exception as e:
                    print('Upload Failed: ')
                    print(e)
                    self.gui.setConnectionStatus(False, len(os.listdir(dir)))
                    
        
    def run(self):
        while not self._stop_req.isSet():
            print('Deamon is looking for new pictures')
            self.upload(self.path,1)
            self.upload(self.privpath,0)
            time.sleep(5)
    
    def stop(self):
        self._stop_req.set();