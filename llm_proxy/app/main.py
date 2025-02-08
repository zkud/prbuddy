from .routers.review import router
from uvicorn import run

from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    run(app, host='127.0.0.1', port=8000, log_level='info')
