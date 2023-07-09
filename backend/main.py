import json
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def printHello():
    return 'Hello World!'
