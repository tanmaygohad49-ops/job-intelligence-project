from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "Job Intelligence API is running"}

# Get all jobs
@app.get("/jobs")
def get_jobs():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()

    conn.close()

    jobs = []
    for row in rows:
        jobs.append({
            "id": row[0],
            "title": row[1],
            "company": row[2],
            "location": row[3],
            "tags": row[4],
            "salary": row[5]
        })

    return {"total_jobs": len(jobs), "data": jobs}