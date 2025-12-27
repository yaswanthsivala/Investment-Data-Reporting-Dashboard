import pandas as pd

# Load consolidated data
df = pd.read_csv('data/processed/consolidated_report.csv')

# Generate asset class summary
asset_summary = df.groupby('asset_class').agg({
    'market_value': ['sum', 'count', 'mean']
}).round(2)
asset_summary.columns = ['total_market_value', 'portfolio_count', 'avg_portfolio_value']
asset_summary = asset_summary.reset_index()

# Compliance summary
compliance_summary = df.groupby('compliance_status_standardized').agg({
    'market_value': 'sum',
    'portfolio_id': 'count'
}).round(2)
compliance_summary.columns = ['total_value', 'portfolio_count']
compliance_summary = compliance_summary.reset_index()

# Trade summary
trade_summary = df.dropna(subset=['trade_type']).groupby('trade_type').agg({
    'trade_amount': ['sum', 'count', 'mean']
}).round(2)
trade_summary.columns = ['total_amount', 'trade_count', 'avg_trade_size']
trade_summary = trade_summary.reset_index()

# Save as separate CSVs or combine
# For simplicity, save asset_summary as summary_reports.csv
asset_summary.to_csv('data/processed/summary_reports.csv', index=False)

print("Summary reports generated.")