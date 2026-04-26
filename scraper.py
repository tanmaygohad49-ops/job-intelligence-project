import requests
import pandas as pd

# API URL for job data
url = "https://remoteok.com/api"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("Starting data scraping...")

# Request data
response = requests.get(url, headers=headers)
data = response.json()

jobs = []

# Skip first element (metadata)
for job in data[1:]:
    jobs.append({
        "title": job.get("position"),
        "company": job.get("company"),
        "location": job.get("location"),
        "tags": ",".join(job.get("tags", [])) if job.get("tags") else "",
        "salary": job.get("salary")
    })

# Convert to DataFrame
df = pd.DataFrame(jobs)

# Save to CSV
df.to_csv("raw_jobs.csv", index=False)

print("Scraping completed successfully. File created: raw_jobs.csv")