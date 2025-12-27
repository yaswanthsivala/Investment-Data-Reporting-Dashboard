# Power BI Dashboard Design

## Dashboard Overview
Interactive dashboard for investment reporting and data quality monitoring.

## Data Sources
- Primary: Snowflake consolidated_reporting view
- Fallback: Processed CSV exports from data/processed/

## Key Visualizations

### 1. Executive Summary Page
- **Total Portfolio Value**: KPI card showing sum of all market values
- **Asset Allocation**: Pie chart showing distribution by asset class
- **Compliance Status**: Donut chart showing pass/fail rates
- **Trade Volume**: Line chart showing trade activity over time

### 2. Portfolio Details Page
- **Portfolio Performance**: Table showing individual portfolio values and changes
- **Client Overview**: Filterable view of client portfolios
- **Asset Class Trends**: Bar chart showing market values by asset class

### 3. Operations Monitoring Page
- **Trade Status**: Status indicators for pending/settled trades
- **Settlement Tracking**: Timeline view of trade settlements
- **Trade Volume by Type**: Bar chart of buy/sell activity

### 4. Compliance & Risk Page
- **Compliance Results**: Heat map of compliance status by portfolio
- **Risk Indicators**: Alerts for failed compliance checks
- **Regulatory Reporting**: Summary of compliance rule adherence

### 5. Data Quality Dashboard
- **Data Completeness**: Percentage of portfolios with complete data
- **Validation Results**: Summary of data validation checks
- **Reconciliation Status**: Indicators for data consistency across sources

## Filters and Slicers
- Date range selector
- Client selector
- Asset class filter
- Compliance status filter

## Refresh Schedule
- Automatic refresh: Daily at 6 AM
- Manual refresh capability
- Data quality alerts on refresh failures

## File Location
- Power BI file: `powerbi/investment_reporting.pbix`
- Data connection: Direct to Snowflake or local CSV files