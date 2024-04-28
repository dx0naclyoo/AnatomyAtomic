from fastapi import FastAPI
from fastapi import Request
from anatomic.Backend import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def read_root(request: Request):
    domain = request.headers.get("Host")
    for head, value in request.headers.items():
        print(head, value)
    return f"API docs - https://{domain}/docs"
