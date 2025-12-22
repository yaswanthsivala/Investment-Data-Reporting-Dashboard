# Investment Data & Reporting Optimization Dashboard

## Overview
This project demonstrates an investment data reporting and analytics solution built using Python.
It focuses on portfolio visibility, asset allocation analysis, and compliance monitoring through
an interactive dashboard.

## Business Problem
Investment and operations teams often rely on manual spreadsheets for portfolio reporting,
which can lead to delays, inconsistencies, and limited analytical insight.
This project shows how reporting can be automated and visualized for faster decision-making.

## Solution
An interactive Streamlit dashboard that provides:
- Executive-level portfolio summary
- Asset allocation breakdown
- Compliance vs non-compliance exposure
- Interactive filtering for deeper analysis

## Tools & Technologies
- Python
- Pandas
- Streamlit
- Matplotlib

## Project Structure
- `data/` – Portfolio and investment data (CSV format)
- `dashboard.py` – Streamlit dashboard application
- `README.md` – Project documentation

## Dashboard Features
- Total portfolio market value
- Asset allocation visualization
- Compliance status analysis
- Interactive asset-class filtering

## How to Run
1. Install dependencies:
   ```bash
   pip install streamlit pandas matplotlib
#Run the dashboard
streamlit run dashboard.py
