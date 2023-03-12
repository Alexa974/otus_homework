from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_route():
    return {"message": "homework_03"}


@app.get("/ping")
def ping():
    return {"message": "pong"}
