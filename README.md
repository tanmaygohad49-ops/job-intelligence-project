# 📊 Job Intelligence Project

## 🚀 Overview
This project is an end-to-end Data Engineering pipeline that collects, processes, stores, and serves real-world job data.

## 🧠 Problem Statement
Businesses need insights about job market trends such as:
- Which skills are in demand
- Which companies are hiring
- Job locations and patterns

This system helps extract and analyze job listings data.

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
- Stores structured data in SQLite database
- Provides REST API for access

## 🚀 How to Run

### 1. Install dependencies
pip install requests pandas fastapi uvicorn

### 2. Run scraper
python scraper.py

### 3. Clean data
python clean.py

### 4. Create database
python database.py

### 5. Run API
uvicorn api:app --reload

## 🌍 API Endpoints
- `/` → Home
- `/jobs` → Get all job data

## 📊 Output
- Clean dataset (CSV)
- SQLite database (jobs.db)
- JSON API response

## 👨‍💻 Author
Data Engineering Internship Project
