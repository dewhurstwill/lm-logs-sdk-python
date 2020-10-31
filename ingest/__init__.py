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
    http_verb = 'POST'
    resource_path = '/log/ingest'
    data = json.dumps(events)

    url = 'https://' + COMPANY_NAME + '.logicmonitor.com/rest' + resource_path
    epoch = str(int(time.time() * 1000))
    request_vars = http_verb + epoch + data + resource_path

    hmac_hex = hmac.new(ACCESS_KEY.encode(),msg=request_vars.encode(),digestmod=hashlib.sha256).hexdigest()
    signature = base64.b64encode(hmac_hex.encode())

    auth = 'LMv1 ' + ACCESS_ID + ':' + signature.decode() + ':' + epoch
    headers = {'Content-Type': 'application/json', 'Authorization': auth}
    
    response = requests.post(url, data=data, headers=headers)
    if (response.status_code != 202): print ('Log failed to send: ', response.content)
