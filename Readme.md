Retail Data Engineering Pipeline for BI Reporting

## Overview
This project implements an end-to-end **Retail Data Engineering Pipeline** that processes raw transactional data and transforms it into actionable business insights using **Python, PostgreSQL, and Power BI**.

The pipeline covers data ingestion, transformation, storage, and visualization.

---

## Problem Statement
Retail businesses generate large volumes of raw data which is not directly usable for decision-making.  
This project builds a structured pipeline to convert raw data into analysis-ready insights.

---

## Objectives
- Build an ETL pipeline using Python
- Clean and transform raw data
- Store processed data in PostgreSQL
- Perform analytical queries using SQL
- Create an interactive Power BI dashboard

---

Raw Data (CSV) -> Python (Pandas ETL) -> PostgreSQL Database -> Power BI Dashboard

---

## Tech Stack
- Python (Pandas, SQLAlchemy)
- PostgreSQL
- SQL
- Power BI
- Git & GitHub

---

#Pipeline Workflow

1. **Data Ingestion**
   - Load raw CSV datasets

2. **Data Cleaning**
   - Handle missing values
   - Remove duplicates
   - Fix data types

3. **Data Transformation**
   - Merge datasets
   - Create master table

4. **Data Storage**
   - Load into PostgreSQL database

5. **Visualization**
   - Build interactive Power BI dashboard

---

## Dashboard Features

- Total Revenue, Orders, Customers, AOV (KPI Cards)
- Monthly Sales Trend Analysis
- Revenue by City
- Orders by City
- Interactive Filters (Date & City)

---

## Dashboard Preview

<img width="955" height="744" alt="image" src="https://github.com/user-attachments/assets/eb4a5ba9-a0a0-4676-95e5-aa9ec6a9e210" />

---


---

## Project Structure

Retail_Data_Engineering_Project/
│
├── src/ # ETL scripts
├── config/ # Configuration files
├── data/ # Raw & processed data
├── logs/ # Logs
├── notebooks/ # Jupyter notebooks
├── schema/ # Database schema
├── README.md
├── requirements.txt


---

## How to Run

1. Clone repository:
    
git clone https://github.com/aditya-dlab/Retail_Data_Engineering_Project.git


3. Activate environment:

venv\Scripts\activate


4. Install dependencies:

pip install -r requirements.txt


5. Run pipeline:

python src/pipeline.py


---

## Note
- This project uses static dataset (batch processing)
- Automation can be added using schedulers (cron/Airflow)

---

## Future Improvements
- Pipeline automation (Airflow / Scheduler)
- Cloud deployment (AWS / Azure)
- Real-time data streaming
- Machine learning integration

---

## Key Learnings
- End-to-end data pipeline design
- Data cleaning and transformation
- SQL and database management
- Business intelligence dashboarding



