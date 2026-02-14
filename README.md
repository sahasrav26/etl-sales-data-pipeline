# End-to-End ETL Pipeline using Apache Airflow, Docker & PostgreSQL

## 📖 Project Overview

This project implements a production-style batch ETL pipeline that:

- Extracts raw sales transaction data from a CSV file
- Cleans and transforms the data
- Validates business rules
- Loads cleaned data into PostgreSQL
- Orchestrates the workflow using Apache Airflow
- Runs fully containerized using Docker Compose

The pipeline processes over 500,000 records.

---

## 🏗 Architecture

Raw CSV (sales.csv)
        ↓
   Extract Task
        ↓
   Transform Task
        ↓
   Validate Task
        ↓
   Load Task
        ↓
   PostgreSQL Database

Orchestration Layer: Apache Airflow  
Containerization: Docker Compose  

---

## 🛠 Tech Stack

- Python
- Pandas
- Apache Airflow
- Docker & Docker Compose
- PostgreSQL
- SQLAlchemy
- psycopg2

---

## 🔄 Pipeline Steps

### 1️⃣ Extract
- Reads raw CSV data
- Logs raw row count

### 2️⃣ Transform
- Removes duplicates
- Removes null values
- Converts Date column to datetime
- Standardizes column names
- Removes negative or zero quantity
- Removes negative or zero price
- Saves cleaned dataset

### 3️⃣ Validate
- Checks required columns
- Checks for null values
- Enforces business rules
- Fails pipeline if validation fails

### 4️⃣ Load
- Connects to PostgreSQL
- Inserts validated data into `sales` table

---

## 📊 Data Volume

- ~536,000 raw records  
- ~531,000 cleaned records  

---

## 🚀 How to Run

1. Initialize Airflow:

docker compose up airflow-init

2. Start all services:

docker compose up

3. Open Airflow UI:

http://localhost:8080

---

## 📌 Key Engineering Concepts Demonstrated

- Batch ETL design
- DAG orchestration
- Data validation gate
- Containerized services
- PostgreSQL integration
- Error handling via Airflow
- Logging for observability
