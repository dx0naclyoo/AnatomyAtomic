from fastapi import FastAPI, Response
from fastapi import Request
from anatomic.Backend import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def read_root(request: Request, response: Response):
    domain = request.headers.get("Host")
    response.set_cookie(key="Custom_Cookies_Test", value="new_value")
    return {
        "API docs": f"https://{domain}/docs/",
        "Headers": request.headers,
        "Cookies": request.cookies,
    }
