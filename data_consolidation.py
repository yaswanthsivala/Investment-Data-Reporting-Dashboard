import pandas as pd

# Load raw data
portfolio_df = pd.read_csv('data/raw/portfolio_data.csv')
operations_df = pd.read_csv('data/raw/operations_data.csv')
compliance_df = pd.read_csv('data/raw/compliance_data.csv')

# Perform the join as in the SQL view
consolidated = portfolio_df.merge(operations_df, on='portfolio_id', how='left')
consolidated = consolidated.merge(compliance_df, on='portfolio_id', how='left')

# Add standardized compliance status
consolidated['compliance_status_standardized'] = consolidated['result'].map({
    'Pass': 'Compliant',
    'Fail': 'Non-Compliant'
}).fillna('Pending')

# Add adjusted market value
consolidated['adjusted_market_value'] = consolidated['market_value'] + consolidated['amount'].fillna(0)

# Filter by date if needed, but data is from 2023
consolidated = consolidated.sort_values(['portfolio_id', 'reporting_date'], ascending=[True, False])

# Select relevant columns
columns = [
    'portfolio_id', 'client_id', 'asset_class', 'market_value', 'trade_type', 'amount', 'result', 'compliance_status_standardized'
]
consolidated = consolidated[columns]
consolidated.columns = [
    'portfolio_id', 'client_id', 'asset_class', 'market_value', 'trade_type', 'trade_amount', 'compliance_result', 'compliance_status_standardized'
]

# Save to processed
consolidated.to_csv('data/processed/consolidated_report.csv', index=False)

print("Consolidated report generated.")