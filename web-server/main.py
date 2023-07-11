import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get ('/contact', response_class = HTMLResponse) #Puedo poner en el Return toda una página
def get_list():
    return """
        <h1>Hola, soy Camilo </h1>
        <p>El creador de este servidor</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()

#uvicorn main:app --reload -----> ejecutar en la terminal