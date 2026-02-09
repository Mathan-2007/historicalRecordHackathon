from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from database import users
from auth import verify_google_token

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/auth/google")
async def google_login(data: dict):
    token = data.get("token")

    user_info = verify_google_token(token)
    if not user_info:
        raise HTTPException(status_code=401, detail="Invalid token")

    email = user_info["email"]
    name = user_info["name"]

    user = users.find_one({"email": email})

    if not user:
        users.insert_one({
            "email": email,
            "name": name,
            "role": "viewer"  # default role
        })
        role = "viewer"
    else:
        role = user["role"]

    return {
        "email": email,
        "role": role
    }
