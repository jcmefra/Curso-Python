import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/products')
    print(r.status_code)