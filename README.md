# 🚀 FastAPI Async vs Sync Performance Demo

This project demonstrates the difference between **synchronous (blocking)** and **asynchronous (non-blocking)** execution in Python using FastAPI.

It compares:

* Sequential API execution (sync)
* Concurrent API execution using `async` / `await`

The goal is to provide a **clear, practical understanding of async programming** and its impact on real-world performance.

---

## 📌 Features

* Side-by-side comparison of sync vs async execution
* Real-world API integration (Joke API)
* Built-in response time measurement
* Minimal, easy-to-understand implementation
* Ideal for learning, demos, and interviews

---

## 🧠 Concepts Covered

* Blocking vs Non-blocking I/O
* Event Loop (core of async execution)
* Coroutines (`async` / `await`)
* Task scheduling using `asyncio.gather()`
* HTTP clients:

  * `requests` (blocking)
  * aiohttp (non-blocking)

---

## ⚙️ Tech Stack

* Python 3.9+
* FastAPI
* Uvicorn (ASGI server)
* asyncio
* aiohttp
* requests

---

## 📂 API Endpoints

### 🔹 `/sync-call`

Simulates blocking calls using `time.sleep()`

* Execution: Sequential
* Expected Time: ~6 seconds

---

### 🔹 `/async-call`

Simulates async behavior using `asyncio.sleep()`

* Execution: Concurrent
* Expected Time: ~2 seconds

---

### 🔹 `/sync-call-api`

Makes real API calls using `requests`

* Execution: Sequential
* External API:
  https://official-joke-api.appspot.com/random_joke
* Expected Time: Sum of all API latencies

---

### 🔹 `/async-call-api`

Makes real API calls using `aiohttp`

* Execution: Concurrent
* Expected Time: ≈ Slowest API response

---

## 📊 Performance Metrics

| Metric               | Sync Version     | Async Version    |
| -------------------- | ---------------- | ---------------- |
| Execution Model      | Blocking         | Non-blocking     |
| Request Handling     | Sequential       | Concurrent       |
| Total Time           | Sum of all calls | Max of all calls |
| Resource Utilization | Idle waiting     | Event-driven     |
| Scalability          | Limited          | High             |
| Throughput           | Low              | High             |

---

## ⏱ Example Results

### Sync API Calls

```json
{
  "total_time": 6.12
}
```

### Async API Calls

```json
{
  "total_time": 2.08
}
```

---

## 🧪 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Deepak-Menan-R/fastapi-async.git
cd fastapi-async
```

### 2. Create virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### 3. Run the server

```bash
uvicorn app.main:app --reload
```

### 4. Open API docs

```
http://127.0.0.1:8000/docs
```

---

## 🔍 Key Takeaways

* Async is **not** multi-threading
* Async is ideal for **I/O-bound tasks**
* `await` allows functions to pause without blocking the system
* `asyncio.gather()` enables concurrent execution of multiple tasks
* Using blocking libraries inside async code removes all benefits

---

## ⚠️ Important Notes

Async improves performance only for:

* API calls
* Database queries
* File I/O

It does **not** help with:

* CPU-intensive computations

---

## 📈 When to Use Async

Use async when:

* Making multiple external API calls
* Building high-concurrency backend systems
* Optimizing latency in I/O-heavy applications

Avoid async when:

* Tasks are CPU-bound
* Simplicity is more important than scalability

---

## 🧭 Future Improvements

* Add load testing (Locust / Apache Bench)
* Compare async vs threading vs multiprocessing
* Add async database integration
* Implement retries and error handling

---

## 👨‍💻 Author

Deepak Menan

Software Engineer | Backend & Systems Enthusiast

---

## ⭐ Support

If this project helped you understand async better, consider giving it a ⭐ on GitHub!

---
