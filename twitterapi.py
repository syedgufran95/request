# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:44:21 2020

@author: MACHINE
"""
from mymodule import *
import os
#nano env/bin/activate
#eport CLIENT_KEYS="YOUR KEY"
#export CLIENT_SECRET="YOUR SECRET"
client_key=os.environ.get("CLIENT_KEYS")
client_secret=os.environ.get("CLIENT_SECRET")
#print("key is ::::::::",client_key)
import base64
key_secret='{}:{}'.format(client_key,client_secret).encode('ascii')
#print(key_secret)
b64_encoded_key=base64.b64encode(key_secret)
b64_encoded_key=b64_encoded_key.decode('ascii')

import requests
base_url='https://api.twitter.com/'
auth_url='{}oauth2/token'.format(base_url)

auth_headers={
    'Authorization':'Basic {}'.format(b64_encoded_key),
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'
    }
auth_data={
        'grant_type':'client_credentials'
    }
    
    

auth_resp=requests.post(auth_url,headers=auth_headers,data=auth_data)

print(code(auth_resp.status_code))
print(auth_resp.json().keys())
access_token=auth_resp.json()['access_token']
search_headers={
    'Authorization':'Bearer {}'.format(access_token)
    }
search_params={
    'q':'trending',
    'result_type':'recent',
    'count':2
    
    
    }
search_url='{}1.1/search/tweets.json'.format(base_url)
search_resp=requests.get(search_url, headers=search_headers,params=search_params)
code(search_resp.status_code)
tweet_data=search_resp.json()
for x in tweet_data['statuses']:
    print(x['text']+'\n')
