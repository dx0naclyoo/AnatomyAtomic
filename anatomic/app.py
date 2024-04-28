from fastapi import FastAPI
from fastapi import Request
from anatomic.Backend import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def read_root(request: Request):
    domain = request.headers.get("Host")
    print(request.headers)
    return f"API docs - https://{domain}/docs"
