# 📊 Job Intelligence Project

## 🚀 Overview
This project is an end-to-end Data Engineering pipeline that collects, processes, stores, and serves real-world job data.

## 🧠 Problem Statement
Businesses need insights about job market trends such as:
- Which skills are in demand  
- Which companies are hiring  
- Job locations and patterns  

This system helps extract and analyze job listings data.

## 💼 Business Value
- Helps companies track hiring trends  
- Identifies in-demand skills  
- Provides structured job data for decision-making  

## 🌐 Data Source
- RemoteOK API

## 🏗️ Architecture
Scraper → Data Cleaning → SQLite Database → FastAPI API

## ⚙️ Tech Stack
- Python  
- Requests  
- Pandas  
- SQLite  
- FastAPI  
- Uvicorn  

## 📦 Features
- Scrapes real job data from API  
- Cleans and processes raw data  
- Handles missing values and duplicates  
- Stores structured data in SQLite database  
- Provides REST API for access  

## 🔄 Pipeline Flow
1. Scrape raw job data  
2. Clean and transform data  
3. Store in SQLite database  
4. Serve via API  

## ⚡ One-Command Setup

Run the complete pipeline:

python scraper.py  
python clean.py  
python database.py  

## 🚀 How to Run

### 1. Install dependencies
pip install requests pandas fastapi uvicorn  

### 2. Run pipeline
python scraper.py  
python clean.py  
python database.py  

### 3. Run API
uvicorn api:app --reload  

## 🌍 API Endpoints
- `/` → Home  
- `/jobs` → Get all job data  

## 📊 Output
- Clean dataset (CSV)  
- SQLite database (`jobs.db`)  
- JSON API response  

## 👨‍💻 Author
Data Engineering Internship Project
