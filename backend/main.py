import os
import json
import uvicorn
import pymysql
from fastapi import FastAPI
from dotenv import load_dotenv

from routers import data

app = FastAPI()

load_dotenv() 

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    db='DB',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

app.include_router(data.router)

@app.get('/')
def printHello():
    return 'Hello World!'

# for test
@app.get("/users")
def get_users():
    try:
        with connection.cursor() as cursor:
            # 쿼리 실행
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()