from fastapi import FastAPI

app = FastAPI()

@app.get("/api/data")
def hello():
    return {"message" : "welcome from FastAPI"}


