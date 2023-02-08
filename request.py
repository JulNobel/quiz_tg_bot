import requests


def get_info():
    api_url = 'https://jservice.io/api/random?count=1'
    response = requests.get(api_url)

    if response.status_code == 200:
        print(response.text)
    else:
        print(response.status_code)
