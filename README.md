# Production-Grade ETL Pipeline with Scheduling

A modular, production-ready ETL (Extract–Transform–Load) pipeline that ingests raw retail transaction data, validates it against a schema, applies business transformations, and loads the cleaned data into a relational database. The pipeline is designed for reliability, maintainability, and scheduled execution in real-world data engineering workflows.

---

## 1. Business Problem

Organizations rely on timely and accurate data for analytics and decision-making. Manual or poorly designed data pipelines often lead to data quality issues, delayed insights, and operational risk.

This project demonstrates how to build a **robust ETL pipeline** that:
- Handles raw data ingestion safely
- Enforces schema consistency
- Applies reusable transformations
- Loads analytics-ready data into a database
- Can be executed reliably as a scheduled job

---

## 2. Architecture Overview

Raw CSV Data
↓
Extract Layer (Schema Validation)
↓
Transform Layer (Cleaning & Business Logic)
↓
Load Layer (Relational Database)
↓
Analytics / Downstream Consumption

---

## 3. Project Structure

etl-pipeline-with-scheduling/
├── data/
│ ├── raw/
│ │ ├── Retail_Transactions_Dataset_sample.csv
│ │ └── schema.json
│ └── processed/
│ ├── Retail_Transactions_Dataset_clean.csv
│ └── retail_transactions.db
├── src/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── run_pipeline.py
├── logs/
├── README.md
└── LICENSE

---

## 4. ETL Pipeline Components

### Extract Layer
- Loads raw CSV data
- Validates columns using a predefined JSON schema
- Ensures consistent structure before transformation

### Transform Layer
- Cleans and standardizes fields
- Applies business rules
- Prepares analytics-ready datasets

### Load Layer
- Persists transformed data into a relational database (SQLite)
- Designed to be easily extended to PostgreSQL or other databases

### Orchestration
- Centralized execution via `run_pipeline.py`
- Clear separation of concerns
- CLI-runnable entrypoint suitable for schedulers (cron, Airflow, Prefect)

---

## 5. How to Run the Pipeline

From the repository root, run:

```bash
python src/run_pipeline.py

```
Expected output:

Loaded XXXX records into database
ETL pipeline completed successfully

6. Technologies Used

- Python
- Pandas
- SQLite
- JSON Schema Validation
- Modular ETL Design

7. Key Engineering Highlights

- Production-style ETL architecture
- Schema-driven ingestion for data quality
- Reusable and testable ETL layers
- Clean orchestration logic
- Debugged and hardened like a real-world pipeline

8. Future Enhancements

- Add workflow scheduling (cron / Airflow / Prefect)
- Introduce logging and alerting
- Extend to cloud data warehouses
- Add data quality checks and metrics

License

This project is licensed under the MIT License.
