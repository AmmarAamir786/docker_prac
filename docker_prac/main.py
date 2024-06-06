from fastapi import FastAPI

app = FastAPI(title="Hello World API")


@app.get("/")
def read_root(): 
    return {"Hello": "World222"}