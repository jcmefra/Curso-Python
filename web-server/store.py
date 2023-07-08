import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/products') #Se hace una solicitud HTTPS con Requests
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['title'])