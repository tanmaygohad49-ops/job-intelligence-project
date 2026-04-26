import pandas as pd

print("Loading raw data...")

df = pd.read_csv("raw_jobs.csv")

# Remove rows with missing important values
df.dropna(subset=["title", "company"], inplace=True)

# Fill missing values
df["location"] = df["location"].fillna("Remote")
df["salary"] = df["salary"].fillna("Not Mentioned")
df["tags"] = df["tags"].fillna("Unknown")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Clean text (remove extra spaces)
df["title"] = df["title"].str.strip()
df["company"] = df["company"].str.strip()

print("Cleaning completed...")

df.to_csv("clean_jobs.csv", index=False)

print("Clean file created: clean_jobs.csv")