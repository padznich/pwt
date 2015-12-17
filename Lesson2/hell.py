# Primary Key: 2bd67fc50b02406da2d259e4ac712cb5
# Secondary Key: 7e0f82134aa84f529bb760e21d1a720e

import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '2bd67fc50b02406da2d259e4ac712cb5',
}

params = urllib.urlencode({
    # Request parameters
    'faceRectangles': '',
})

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/emotion/v1.0/recognize&%s" % params, "https://securevpn.com/assets/img/humans.png", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))