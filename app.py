from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():

    try:
        with open("newsletter.html", "r", encoding="utf-8") as file:
            return file.read()

    except Exception as e:
        return f"""
        <h1>ERROR LOADING NEWSLETTER</h1>
        <p>{str(e)}</p>
        """
