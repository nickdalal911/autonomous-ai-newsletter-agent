from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():

    with open("newsletter.html", "r", encoding="utf-8") as file:
        return file.read()