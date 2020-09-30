#!/bin/env python

import os
import requests
import json
import hashlib
import base64
import time
import hmac

ACCESS_ID = os.environ['ACCESS_ID']
ACCESS_KEY = os.environ['ACCESS_KEY']
COMPANY_NAME = os.environ['COMPANY_NAME']

def ingest(events):
    httpVerb = 'POST'
    resourcePath = '/log/ingest'
    data = json.dumps(events)

    url = 'https://' + COMPANY_NAME + '.logicmonitor.com/rest' + resourcePath
    epoch = str(int(time.time() * 1000))
    requestVars = httpVerb + epoch + data + resourcePath

    hmacHex = hmac.new(ACCESS_KEY.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
    signature = base64.b64encode(hmacHex.encode())

    auth = 'LMv1 ' + ACCESS_ID + ':' + signature.decode() + ':' + epoch
    headers = {'Content-Type': 'application/json', 'Authorization': auth}
    
    response = requests.post(url, data=data, headers=headers)
    if (response.status_code != 202): print ('Log failed to send: ', response.content)