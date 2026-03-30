from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# http://127.0.0.1:8000/test1
@app.get("/test1")
async def funcaoteste():
    return {"message": "Sera que?"}

