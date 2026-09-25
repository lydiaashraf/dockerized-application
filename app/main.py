from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.get("/")
def home():
    return {"message": "Hello from Docker Project"}

@app.get("/cache")
def cache_data():
    r.set("message", "Hello from Redis")
    return {"message": r.get("message")}