# Real-time crypto market data pipeline
## Description
This project implements an end-to-end data engineering pipeline that collects real-time cryptocurrency market data from Binance via WebSocket, streams it through Apache Kafka, processes and validates it, and stores it in a PostgreSQL database. The entire infrastructure runs in Docker containers and is orchestrated with Apache Airflow. The collected data 
is visualized through a Power BI dashboard. The pipeline is written in Python 
using object-oriented principles and follows software engineering best practices 
including CI/CD via GitHub Actions.

## Architecture

Binance WebSocket → Kafka → Python Consumer (validation & transformation) → PostgreSQL → Power BI

## Tech Stack
- Python
- Apache Kafka
- Apache Airflow
- PostgreSQL
- Docker & Docker Compose
- Power BI
- GitHub Actions (CI/CD)

## How to run

```bash
git clone https://github.com/evagvr/crypto-pipeline
cd crypto-pipeline
cp .env.example .env
# Edit .env with your credentials
docker compose up --build
```
After startup, Airflow is available at http://localhost:8080 (user: admin, password: admin).

## Dashboard
