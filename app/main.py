from fastapi import FastAPI
import redis
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

r = redis.Redis(host="redis", port=6379, decode_responses=True)
#e3ml redis client w 5azno fi variable r 
#redis.Redis y3ny e3ml redis client 3lshan a2dr ast5dmo m3 .Redis
# Redis di class mawgooda gowa el Python redis package
#fastapi bt2ol hena ro7 ll container eli service bta3to esmha redis
#6379 dh el default port bta3 redis
#decode_responses=True Di ma3naha en Redis client yeragga3ly el values ka strings badal ma yeragga3ha ka bytes

@app.get("/")
def home():
    return {"message": "Hello from Docker Project"}

@app.get("/cache")
def cache_data():
    r.set("message", "Hello from Redis")
    return {"message": r.get("message")}

@app.post("/users")
def create_user(user: User):
    r.set(f"user:{user.email}", user.model_dump_json())

    return {
        "message": "User created successfully",
        "user": user
    }

@app.get("/users/{email}")
def get_user(email: str):
    data = r.get(f"user:{email}")

    if data is None:
        return {"message": "User not found"}

    return {
        "user": data
    }