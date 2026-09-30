from fastapi import FastAPI  # pyright: ignore[reportMissingImports]
from .db.database import create_table

create_table()

app = FastAPI()

@app.get("/")
def run_root():
    return {"message": "api is running"}