from fastapi import FastAPI



app = FastAPI()


@app.get("/")
async def hello_world():
    return {"Message": "Hello World V2!!"}


@app.get("/ping")
async def ping():
    return {"Message": "Pong"}