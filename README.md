**End-to-End ETL Pipeline using Apache Airflow, Docker & PostgreSQL**

**Project Overview**

This project implements a production-style batch ETL pipeline that:
- Extracts raw sales transaction data from a CSV file
- Cleans and transforms the data
- Validates business rules
- Loads cleaned data into PostgreSQL
- Orchestrates the workflow using Apache Airflow
- Runs fully containerized using Docker Compose

The pipeline processes over 500,000 records.

---

**Architecture:**

Raw CSV → Extract → Transform → Validate → Load → PostgreSQL

All steps are orchestrated using Airflow running inside Docker containers.

Orchestration Layer: Apache Airflow  
Containerization: Docker Compose  

---

**Tech Stack:**
- Python
- Pandas
- Apache Airflow
- Docker & Docker Compose
- PostgreSQL
- SQLAlchemy
- psycopg2

---

**Pipeline Steps-**

***1.Extract***
- Reads raw CSV data
- Logs raw row count

***2.Transform***
- Removes duplicates
- Removes null values
- Converts Date column to datetime
- Standardizes column names
- Removes negative or zero quantity
- Removes negative or zero price
- Saves cleaned dataset

***3.Validate***
- Checks required columns
- Checks for null values
- Enforces business rules
- Fails pipeline if validation fails

***4.Load***
- Connects to PostgreSQL
- Inserts validated data into `sales` table

---

**Data Volume**
- ~536,000 raw records  
- ~531,000 cleaned records  

---

**How to Run**
1. Initialize Airflow:
docker compose up airflow-init

2. Start all services:
docker compose up

3. Open Airflow UI:
http://localhost:8080

---

**Key Features-**
- Automated ETL workflow using Apache Airflow
- Data extraction from CSV source files
- Data cleaning and transformation using Pandas
- Data validation checks before loading
- Loading processed data into PostgreSQL
- Fully containerized setup using Docker
- Modular and scalable project structure
