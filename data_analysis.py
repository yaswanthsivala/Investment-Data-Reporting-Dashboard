# Data Analysis Script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from our processed consolidated report
df = pd.read_csv('data/processed/consolidated_report.csv', comment='#')

# Basic analysis
print("=== Portfolio Analysis Results ===")
print(f"Total portfolios analyzed: {len(df)}")
print(f"Total market value: ${df['market_value'].sum():,.2f}")
print(f"Average portfolio value: ${df['market_value'].mean():,.2f}")
print(f"Median portfolio value: ${df['market_value'].median():,.2f}")

print("\n=== Asset Class Distribution ===")
asset_summary = df.groupby('asset_class')['market_value'].agg(['count', 'sum', 'mean']).round(2)
asset_summary.columns = ['Portfolio Count', 'Total Value', 'Average Value']
print(asset_summary)

print("\n=== Compliance Status ===")
compliance_summary = df.groupby('compliance_status_standardized')['market_value'].agg(['count', 'sum']).round(2)
compliance_summary.columns = ['Portfolio Count', 'Total Value']
print(compliance_summary)

# Visualization
plt.figure(figsize=(12, 8))

# Subplot 1: Asset Class Distribution
plt.subplot(2, 2, 1)
asset_totals = df.groupby('asset_class')['market_value'].sum()
plt.pie(asset_totals, labels=asset_totals.index, autopct='%1.1f%%')
plt.title('Asset Allocation by Market Value')

# Subplot 2: Portfolio Value Distribution
plt.subplot(2, 2, 2)
plt.hist(df['market_value'], bins=10, edgecolor='black')
plt.title('Portfolio Value Distribution')
plt.xlabel('Market Value ($)')
plt.ylabel('Frequency')

# Subplot 3: Compliance Status
plt.subplot(2, 2, 3)
compliance_counts = df['compliance_status_standardized'].value_counts()
plt.bar(compliance_counts.index, compliance_counts.values, color=['green', 'red'])
plt.title('Compliance Status Distribution')
plt.ylabel('Number of Portfolios')

# Subplot 4: Trade Activity
plt.subplot(2, 2, 4)
trade_counts = df['trade_type'].value_counts()
plt.bar(trade_counts.index, trade_counts.values)
plt.title('Trade Activity by Type')
plt.ylabel('Number of Trades')

plt.tight_layout()
plt.savefig('docs/investment_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✓ Analysis complete! Charts saved to docs/investment_analysis.png")