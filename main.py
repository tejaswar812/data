from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

app = FastAPI()

# Allow frontend from any origin (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root@123",
    "database": "datacollection"
}

@app.post("/submit")
def submit_form(name: str = Form(...), email: str = Form(...)):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO user1 (name, email) VALUES (%s, %s)"
    cursor.execute(sql, (name, email))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Data submitted successfully"}
