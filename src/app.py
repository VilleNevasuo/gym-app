
from fastapi import FastAPI
import uvicorn
from db import SessionLocal, engine
from api.v1.api import api_router
from db import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hello Wo    rld"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="info")