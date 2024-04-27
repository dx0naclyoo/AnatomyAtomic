from fastapi import FastAPI
from fastapi import Request

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    domain = request.headers.get("Host")
    print(request.headers)
    return f"API docs - https://{domain}/docs"
