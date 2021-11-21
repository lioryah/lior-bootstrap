from typing import Optional
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


def reverse(s: str):
    res = s[::-1]
    return res

@app.get("/reverse/{item_id}")
def reverse_it(item_id: str, q: Optional[str] = None):
    res = reverse(item_id)
    return {"reversee": res}


def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)

def main_():
    import fire
    fire.Fire()


if __name__ == '__main__':
    start_server()
    # main_()