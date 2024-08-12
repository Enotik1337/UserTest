from fastapi import FastAPI, Query, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, RedirectResponse

#uvicorn main:app --reload

app = FastAPI(debug=True)


# class User(BaseModel):
#     login: str
#     name: str
#     surname: str
#     age: int

users = [
    {'login': 'test', 'name': 'Jonh', 'surname': 'Smith', 'age': 30}
    ]

@app.get("/")
def index():
    html = "<h1>Users Storage</h1>"
    for user in users:
        html += "<p>" + user['login'] + " " + user['name'] + "</p>"