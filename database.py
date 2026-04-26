import sqlite3
import pandas as pd

print("Loading cleaned data...")

df = pd.read_csv("clean_jobs.csv")

# Create database connection
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    tags TEXT,
    salary TEXT
)
""")

# Insert data into table
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO jobs (title, company, location, tags, salary)
    VALUES (?, ?, ?, ?, ?)
    """, (row["title"], row["company"], row["location"], row["tags"], row["salary"]))

conn.commit()
conn.close()

print("Database created successfully: jobs.db")