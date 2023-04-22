import requests
from requests.auth import HTTPBasicAuth

DNAC_URL = "sandboxdnac.cisco.com"
DNAC_USER = "devnetuser"
DNAC_PASS = ""

def get_auth_token():
     """
     Building out Auth request. Using requests.post to make a call to the Auth Endpoint
     """
     url = 'https://{}/dna/system/api/v1/auth/token'.format(DNAC_URL)                      # Endpoint URL
     hdr = {'content-type' : 'application/json'}                                           # Define request header
     resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASS), headers=hdr)      # Make the POST Request
     token = resp.json()['Token']                                                          # Retrieve the Token
     print("Token Retrieved: {}".format(token))                                            # Print out the Token
     return token   