from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests
from requests.auth import HTTPBasicAuth
import json
from emailClient import EmailClient


class RequestWrapper:

    # def __init__(self): 
    #     # resp = requests.get('http://34.73.210.226/api/token', auth=HTTPBasicAuth('foobar@foobar.com', 'foobar'))
    #     # # token = resp['token'] 
    #     # # requests.post('http://34.73.210.226/api/item', auth=HTTPBasicAuth(token, None))
    #     # json_rsp = json.loads(resp.content)
    #     # self.__token = json_rsp['token']
    #     # self.__email_client = EmailClient()

    #     # if resp.status_code != 201 and resp.status_code != 200:
    #     #     __message = f'Error inserting into DB due to authentication with code {resp.status_code}'
    #     #     self.__email_client.sendErrorMessage(__message)
            
        
    def insert_into_db(self, item_object):
        # querystring = {"name":item_object['item'],"price":item_object['price'],"website_name":item_object['website'] ,"image_url":item_object["image_link"],"url":item_object['item_link']}
        # response = requests.post('http://34.73.210.226/api/item', params=querystring, auth=HTTPBasicAuth(self.__token, None))
        # __response = json.loads(response.content)
        
        # if response.status_code == 409 and float(__response['price']) > float(item_object['price']): # checks if item is duplicate then if it is on sale
        #     new_resp = requests.put(f'http://34.73.210.226/api/item/{__response["item_id"]}?price={item_object["price"]}')
        #     __new_resp = json.loads(new_resp.content)
        #     __emails = __new_resp['emails'] 

        #     # uncomment to test email
        #     # __message = f'Subject: Wishlist Item Sale!\n\nOne of your Items on your wishlist is on sale! {item_object["item"]} for the price {item_object["price"]}'
        #     # self.__email_client.sendMessage(__message)
            
        #     for email in __emails:
        #         __message = f'Subject: Wishlist Item Sale!\n\nOne of your Items on your wishlist is on sale! {item_object["item"]} for the price {item_object["price"]}'
        #         self.__email_client.sendMessage(__message, email)

        # elif response.status_code != 201 and response.status_code != 200 and response.status_code != 409: #sends an error email if the status code returned is not expected
        #     __message = f'Error inserting into DB from {item_object} with code {response.status_code}'
        #     self.__email_client.sendErrorMessage(__message)
        response = "test"
        return response