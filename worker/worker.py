import time
import redis
import os
import json

# Connect to Redis using the environment variable from docker-compose
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

print("Worker started and listening for tasks...")

while True:
    # 'blpop' blocks until a task is available in 'request_queue'
    task = r.blpop("request_queue", timeout=5)
    
    if task:
        _, data = task
        payload = json.loads(data)
        print(f"Processing task: {payload['text']}")
        # Add your model inference logic here
    else:
        print("Waiting for tasks...")