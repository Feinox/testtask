import requests


class Client:
    url = 'http://127.0.0.1:5000/number'
    response = requests.get(url)
    print(response.text)
