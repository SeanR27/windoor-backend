from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="App Instance Name")

@app.get("/")
def read_root():
    return {"message": "Hello from the FastAPI backend!"}

origins = [
    "http://localhost:5173", # Use the frontend local host for development
    "myapp.com" # Use actual frontend URL for deployment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)