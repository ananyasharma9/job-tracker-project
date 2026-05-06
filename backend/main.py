from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB connection function
def get_connection():
    return psycopg2.connect(
    host="jobtracker.cvoguqiialth.ap-south-1.rds.amazonaws.com",
    database="jobtracker",
    user="postgres",
    password="Ananyasharma",
    port="5432"
    )

class Job(BaseModel):
    company: str
    role: str
    status: str

# GET jobs
@app.get("/jobs")
def get_jobs():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT company, role, status FROM jobs;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    jobs = []
    for row in rows:
        jobs.append({
            "company": row[0],
            "role": row[1],
            "status": row[2]
        })

    return jobs

# POST job
@app.post("/jobs")
def add_job(job: Job):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO jobs (company, role, status) VALUES (%s, %s, %s);",
        (job.company, job.role, job.status)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Job added successfully"}