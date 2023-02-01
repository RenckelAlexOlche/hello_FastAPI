from fastapi import FastAPI

app = FastAPI()

app.title = 'LOL'

@app.get('/', tags=['index'])
def index():
    return 'Hello World!'