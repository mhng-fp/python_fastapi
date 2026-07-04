from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
from app.shortener import shorten, resolve

app = FastAPI()

# Enable CORS for your React frontend container
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def read_root():
    # The key must be exactly "message" wrapped in a dictionary
    return {"message": "Hello there!"}

class URLRequest(BaseModel):
    long_url: HttpUrl

@app.post("/shorten")
def shorten_url(request: URLRequest):
    long_url_str = str(request.long_url)
    short_url = shorten(long_url_str)
    return {"short_url": short_url}

@app.get("/{short_code}")
def resolve_url(short_code: str):
    long_url = resolve(short_code)

    if not long_url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url=long_url)

