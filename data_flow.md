# Data Flow Documentation

## Data Pipeline Architecture

### 1. Data Ingestion
- **Source**: Raw CSV/Excel files from multiple systems
- **Location**: `data/raw/` folder
- **Files**:
  - `portfolio_data.csv`: Client portfolios, asset classes, market values
  - `operations_data.csv`: Trade transactions, settlements
  - `compliance_data.csv`: Regulatory compliance checks

### 2. Data Storage (Snowflake)
- **Tables Created**:
  - `portfolio_data`
  - `operations_data`
  - `compliance_data`
- **Location**: Snowflake database
- **Purpose**: Centralized data warehouse for consolidation

### 3. Data Transformation (SQL)
- **Location**: `sql/` folder
- **Processes**:
  - Data cleansing and standardization
  - Joining datasets across sources
  - Aggregation for reporting metrics
  - Column name harmonization

### 4. Data Validation (Python)
- **Location**: `scripts/` folder
- **Scripts**: `data_validation.py`
- **Checks**:
  - Missing values detection
  - Data type validation
  - Cross-source reconciliation
  - Business rule validation

### 5. Data Visualization (Power BI)
- **Source**: Processed data from Snowflake or CSV exports
- **Location**: `powerbi/` folder
- **Outputs**:
  - Interactive dashboards
  - Key metrics tracking
  - Trend analysis
  - Data quality indicators

### 6. Business Delivery (Excel)
- **Location**: `excel/` folder
- **Purpose**: Static reports for business users
- **Format**: Client summaries, pivot tables

## Data Flow Diagram
```
Raw Data (CSV) → Snowflake Tables → SQL Transforms → Python Validation → Power BI Dashboards
                                      ↓
                               Excel Reports
```

## Quality Gates
- Data loaded into Snowflake with schema validation
- SQL transformations ensure data consistency
- Python scripts validate business rules
- Power BI connects to validated data only
- Excel reports generated from approved datasets