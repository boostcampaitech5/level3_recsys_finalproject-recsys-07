from fastapi import FastAPI

from routers import data

app = FastAPI()

app.include_router(data.router)


@app.get("/")
def printHello():
    return "Hello World!"
