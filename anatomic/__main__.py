import uvicorn
from settings import settings

if __name__ == "__main__":
    uvicorn.run("app:app", host=settings.app.host, port=settings.app.port, reload=True)
