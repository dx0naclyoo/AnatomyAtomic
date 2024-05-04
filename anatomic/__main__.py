import uvicorn
from anatomic.settings import settings

if __name__ == "__main__":
    uvicorn.run(
        "anatomic.app:app", host=settings.app.host, port=settings.app.port, reload=True
    )
