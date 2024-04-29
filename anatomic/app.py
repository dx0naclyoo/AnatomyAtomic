from typing import Callable

from fastapi import FastAPI, Response, APIRouter, Request
from fastapi.routing import APIRoute

from starlette.middleware.cors import CORSMiddleware

from anatomic.Backend import router

app = FastAPI()
app.include_router(router)


# Handle CORS
class CORSHandler(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def preflight_handler(request: Request):
            if request.method == 'OPTIONS':
                response = Response()
                response.headers['Access-Control-Allow-Origin'] = '*'
                response.headers['Access-Control-Allow-Methods'] = 'POST, GET, DELETE, OPTIONS'
                response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
            else:
                response = await original_route_handler(request)

        return preflight_handler


router = APIRouter(route_class=CORSHandler)
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================


@app.get("/")
def read_root(request: Request, response: Response):
    domain = request.headers.get("Host")
    response.set_cookie(key="Custom_Cookies_Test", value="new_value")
    return {
        "API docs": f"https://{domain}/docs/",
        "Headers": request.headers,
        "Cookies": request.cookies,
    }
