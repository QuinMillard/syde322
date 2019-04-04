from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests
from requests.auth import HTTPBasicAuth
import json


class RequestWrapper:

    def __init__(self): 
        resp = requests.get('http://34.73.210.226/api/token', auth=HTTPBasicAuth('foobar@foobar.com', 'foobar'))
        # token = resp['token'] 
        # requests.post('http://34.73.210.226/api/item', auth=HTTPBasicAuth(token, None))
        json_rsp = json.loads(resp.content)
        self.__token = json_rsp['token']
        
    def insert_into_db(self, item_object):
        querystring = {"name":item_object['item'],"price":item_object['price'],"website_name":item_object['website'] ,"image_url":item_object["image_link"],"url":item_object['item_link']}
        response = requests.post('http://34.73.210.226/api/item', params=querystring, auth=HTTPBasicAuth(self.__token, None))
        return response