from fastapi import FastAPI
import time
import asyncio
import aiohttp
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/sync-call")
def sync_call():
    to_call = ["call1", "call2", "call3"]
    results = []
    start_time = time.time()
    for call in to_call:
        # Simulate a synchronous call
        result = f"Result from {call}"
        time.sleep(2)
        results.append(result)
    total_time = time.time() - start_time
    return {"results": results, "total_time": total_time}


@app.get("/async-call")
async def async_call():
    to_call = ["call1", "call2", "call3"]
    start_time = time.time()
    
    async def make_call(call):
        await asyncio.sleep(2)
        return f"Result from {call}"
    
    # Run all calls concurrently
    results = await asyncio.gather(*[make_call(c) for c in to_call])
    
    total_time = time.time() - start_time
    return {"results": list(results), "total_time": total_time}

@app.get("/async-call-api")
async def async_call_api():
    urls = [
        "https://official-joke-api.appspot.com/random_joke",
        "https://official-joke-api.appspot.com/random_joke",
        "https://official-joke-api.appspot.com/random_joke"
    ]

    start_time = time.time()

    async def make_call(session, url):
        async with session.get(url) as response:
            data = await response.json()
            return data["setup"] + " - " + data["punchline"]

    async with aiohttp.ClientSession() as session:
        tasks = [make_call(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    total_time = time.time() - start_time
    return {"results": results, "total_time": total_time}

@app.get("/sync-call-api")
def sync_call_api():
    urls = [
        "https://official-joke-api.appspot.com/random_joke",
        "https://official-joke-api.appspot.com/random_joke",
        "https://official-joke-api.appspot.com/random_joke"
    ]

    start_time = time.time()
    results = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        results.append(data["setup"] + " - " + data["punchline"])
    
    total_time = time.time() - start_time
    return {"results": results, "total_time": total_time}