from fastapi import FastAPI
import redis, os, json

app = FastAPI()

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(text: str):
    r.lpush("request_queue", json.dumps({"text": text}))
    return {"status": "queued"}