# http://stuvel.eu/media/flickrapi-docs/documentation/

import flickrapi
import webbrowser

class flickrConnect():
    
    def __init__(self):
        self.api_key = u'9460c8c076928bf8239504139c1e8c88'
        self.api_secret = u'042eb1bdb5531c1f'

        self.flickr = flickrapi.FlickrAPI(self.api_key, self.api_secret)

    def checkAuthentication(self):
        try:
            print('Flickr Authentification')
            # Only do this if we don't have a valid token already
            if not self.flickr.token_valid(perms=u'write'):
                print('Get request Token')
                # Get a request token
                self.flickr.get_request_token(oauth_callback=u'oob')
        
                # Open a browser at the authentication URL. Do this however
                # you want, as long as the user visits that URL.
                authorize_url = self.flickr.auth_url(perms=u'write')
                webbrowser.open_new_tab(authorize_url)
        
                # Get the verifier code from the user. Do this however you
                # want, as long as the user gives the application the code.
                verifier = unicode(raw_input('Verifier code: '))
                #
                # Trade the request token for an access token
                self.flickr.get_access_token(verifier)                
                print('Authentification successfull')

        except Exception as e:
            print('Authentification Exception: ') 
            print(e)
            

    def upload(self, filename, is_public):
        try:
            self.checkAuthentication()
            print('Upload Photo')
            resp = self.flickr.upload(filename=filename, is_public=is_public, tags='''germanphotobooth "wsj2015" "wsj2015de"''')
            return resp
            
        except Exception as e:
            print('Connection Error in Upload')
            print(e)
            

            
            
        