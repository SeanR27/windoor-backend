from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="App Instance Name")

@app.get("/")
def read_root():
    return {"message": "Hello from the FastAPI backend!"}

origins = [
    "http://localhost:5173", # Development
    "https://prc-management.vercel.app/" # Deployment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)