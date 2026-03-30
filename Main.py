from fastapi import FastAPI

app = FastAPI()


@app.get("/helloword")
async def root():
    return {"message": "Hello World"}


@app.get("/funcaotest1")
async def funcaoteste():
    return {"message": "Sera que?"}

