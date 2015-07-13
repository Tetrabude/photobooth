# http://stuvel.eu/media/flickrapi-docs/documentation/

import flickrapi
import webbrowser

api_key = u'9460c8c076928bf8239504139c1e8c88'
api_secret = u'042eb1bdb5531c1f'

flickr = flickrapi.FlickrAPI(api_key, api_secret)

def checkAuthentication():
    print('Check Flickr Authentification')
    # Only do this if we don't have a valid token already
    if not flickr.token_valid(perms='write'):

        # Get a request token
        flickr.get_request_token(oauth_callback='oob')

        # Open a browser at the authentication URL. Do this however
        # you want, as long as the user visits that URL.
        authorize_url = flickr.auth_url(perms='write')
        webbrowser.open_new_tab(authorize_url)

        # Get the verifier code from the user. Do this however you
        # want, as long as the user gives the application the code.
        verifier = input('Verifier code: ')
#
        # Trade the request token for an access token
        flickr.get_access_token(verifier)
        
        print('Authentification successfull')
    else:
        print('Already Authentificated')

def upload(filename):
    print('Start Authentification')
    checkAuthentication()

    resp = flickr.upload(filename)

    print(resp)