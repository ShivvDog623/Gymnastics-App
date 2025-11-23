from fastapi import FastAPI


app = FastAPI(title="Gymnastics App API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Welcome to the Gymnastics App API!"}