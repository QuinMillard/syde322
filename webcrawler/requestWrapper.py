from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests
from requests.auth import HTTPBasicAuth
import json
from emailClient import EmailClient


class RequestWrapper:

    def __init__(self): 
        resp = requests.get('http://34.73.210.226/api/token', auth=HTTPBasicAuth('foobar@foobar.com', 'foobar'))
        # token = resp['token'] 
        # requests.post('http://34.73.210.226/api/item', auth=HTTPBasicAuth(token, None))
        json_rsp = json.loads(resp.content)
        self.__token = json_rsp['token']
        self.__email_client = EmailClient()
        
    def insert_into_db(self, item_object):
        querystring = {"name":item_object['item'],"price":item_object['price'],"website_name":item_object['website'] ,"image_url":item_object["image_link"],"url":item_object['item_link']}
        response = requests.post('http://34.73.210.226/api/item', params=querystring, auth=HTTPBasicAuth(self.__token, None))
        __response = json.loads(response.content)
        print(__response)
        if response.status_code == 409 and float(__response['price']) >= float(item_object['price']):
            new_resp = requests.put(f'http://34.73.210.226/api/item/{__response["item_id"]}?price={item_object["price"]}')
            __new_resp = json.loads(new_resp.content)
            __emails = __new_resp['emails'] # send emails to this list it is an array
            # print(__emails)
            # __message = f'One of your Items on your wishlist is on sale! {item_object["item"]} for the price {item_object["price"]}' 
            # self.__email_client.sendMessage(__message)
            
            for email in __emails:
                __message = f'One of your Items on your wishlist is on sale! {item_object["item"]} for the price {item_object["price"]}'
                self.__email_client.sendMessage(__message, email)


        return response