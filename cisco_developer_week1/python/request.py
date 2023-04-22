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

def get_device_list():
    """
    Building out function to retrieve list of devices. Using requests.get to make a call to the network device Endpoint
    """
    token = get_auth_token()                                                               # Get Token
    url = "https://{}/dna/intent/api/v1/network-device".format(DNAC_URL)                   # Network Device endpoint
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}                     # Build header Info
    resp = requests.get(url, headers=hdr)                                                  # Make the Get Request
    device_list = resp.json()                                                              # Capture the data from the controller
    print_device_list(device_list)    

def print_device_list(device_json):
     print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
          format("hostname", "mgmt IP", "serial","platformId", "SW Version", "role", "Uptime"))
     for device in device_json['response']:
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        if device['serialNumber'] is not None and "," in device['serialNumber']:
            serialPlatformList = zip(device['serialNumber'].split(","), device['platformId'].split(","))
        else:
            serialPlatformList = [(device['serialNumber'], device['platformId'])]
        for (serialNumber, platformId) in serialPlatformList:
            print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
                  format(device['hostname'],
                         device['managementIpAddress'],
                         serialNumber,
                         platformId,
                         device['softwareVersion'],
                         device['role'], uptime))