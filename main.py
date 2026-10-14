from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Addition API")


class AddRequest(BaseModel):
    a: float
    b: float


@app.get("/add")
def add_get(a: float, b: float):
    return {"a": a, "b": b, "result": a + b}


@app.post("/add")
def add_post(req: AddRequest):
    return {"a": req.a, "b": req.b, "result": req.a + req.b}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
