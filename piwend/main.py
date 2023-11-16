from datetime import datetime

from app import App
from responseType import HTMLResponse, JsonResponse

PORT = 80
HOST = "127.0.0.1"
CHUNK_SIZE = 1024

app = App()
app.setup(HOST, PORT)


@app.get("/")
def home() -> HTMLResponse:
    with open("html/index.html") as f:
        return f.read()


@app.get("/add/{a}/{b}")
def add(a: int, b: int) -> str:
    return str(a + b)


@app.get("/datetime")
def get_date_time() -> JsonResponse:
    return datetime.now()


@app.get("/about")
def about() -> str:
    with open("html/about.html") as f:
        return f.read()


if __name__ == "__main__":
    app.run()
