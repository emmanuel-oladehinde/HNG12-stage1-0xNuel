from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.get("/health")
async def health():
    return {"message": "healthy"}

@app.get("/me")
async def me():
    return {
        "name": "Emmanuel Oladehinde",
        "email": "oladehindeemmnauel9@gmail.com",
        "github": "https://github.com/emmanuel-oladehinde"
    }
