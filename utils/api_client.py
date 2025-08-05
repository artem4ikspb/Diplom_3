import requests
from data.urls import Urls
from json.decoder import JSONDecodeError



class APIClient:

    @staticmethod
    def create_user(payload):
        url = Urls.CREATE_USER_URL
        resp = requests.post(url, data=payload)
        try:
            return resp.status_code, resp.json()
        except JSONDecodeError:
            return resp.status_code, resp.text      

    @staticmethod
    def delete_user(headers):
        url = Urls.DELETE_USER_URL
        resp = requests.delete(url, headers=headers)
        try:
            return resp.status_code, resp.json()
        except JSONDecodeError:
            return resp.status_code, resp.text      
