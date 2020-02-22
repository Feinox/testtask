import requests

class Client():

    def __init__(self):
        url = 'http://127.0.0.1:5000/number'
        self.request = requests.get(url)