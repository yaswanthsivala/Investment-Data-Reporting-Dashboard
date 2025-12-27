import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_excel_summary():
    """Generate Excel-ready summary for business users"""
    print("Step 3: Generating Excel Summary Report...")

    # Load processed data
    consolidated_df = pd.read_csv('data/processed/consolidated_report.csv', comment='#')

    # Create client summary
    client_summary = consolidated_df.groupby('client_id').agg({
        'market_value': 'sum',
        'portfolio_id': 'count',
        'compliance_status_standardized': lambda x: (x == 'Compliant').sum() / len(x) * 100
    }).round(2)

    client_summary.columns = ['Total_Value', 'Portfolio_Count', 'Compliance_Rate_Pct']
    client_summary = client_summary.reset_index()

    # Create asset class summary
    asset_summary = consolidated_df.groupby('asset_class').agg({
        'market_value': ['sum', 'count', 'mean']
    }).round(2)
    asset_summary.columns = ['total_market_value', 'portfolio_count', 'avg_portfolio_value']
    asset_summary = asset_summary.reset_index()

    # Save to Excel format (CSV for compatibility)
    client_summary.to_csv('excel/client_portfolio_summary.csv', index=False)
    asset_summary.to_csv('excel/asset_class_summary.csv', index=False)

    print("✓ Excel summaries generated successfully")
    print(f"  - Client summary: {len(client_summary)} clients")
    print(f"  - Asset class summary: {len(asset_summary)} categories")

    return client_summary, asset_summary

def create_visualizations():
    """Create key visualizations"""
    print("\nStep 4: Creating Data Visualizations...")

    # Load data
    consolidated_df = pd.read_csv('data/processed/consolidated_report.csv')
    summary_df = pd.read_csv('data/processed/summary_reports.csv', nrows=6)

    # Set style
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # Asset Allocation Pie Chart
    axes[0,0].pie(summary_df['total_market_value'],
                  labels=summary_df['asset_class'],
                  autopct='%1.1f%%',
                  startangle=90)
    axes[0,0].set_title('Asset Allocation by Market Value')

    # Compliance Status Bar Chart
    compliance_data = pd.read_csv('data/processed/summary_reports.csv', skiprows=7, nrows=2)
    axes[0,1].bar(compliance_data['compliance_status_standardized'],
                  compliance_data['total_value'],
                  color=['green', 'red'])
    axes[0,1].set_title('Compliance Status Distribution')
    axes[0,1].set_ylabel('Total Market Value')
    axes[0,1].ticklabel_format(style='plain', axis='y')

    # Trade Activity
    trade_data = pd.read_csv('data/processed/summary_reports.csv', skiprows=10, nrows=2)
    axes[1,0].bar(trade_data['trade_type'], trade_data['total_amount'])
    axes[1,0].set_title('Trade Activity by Type')
    axes[1,0].set_ylabel('Total Amount')

    # Portfolio Value Distribution
    axes[1,1].hist(consolidated_df['market_value'], bins=10, edgecolor='black')
    axes[1,1].set_title('Portfolio Value Distribution')
    axes[1,1].set_xlabel('Market Value')
    axes[1,1].set_ylabel('Frequency')

    plt.tight_layout()
    plt.savefig('docs/portfolio_analysis_charts.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("✓ Visualizations created and saved to docs/portfolio_analysis_charts.png")

def generate_powerbi_data():
    """Prepare data for Power BI consumption"""
    print("\nStep 5: Preparing Power BI Data Files...")

    # Load consolidated data
    df = pd.read_csv('data/processed/consolidated_report.csv')

    # Create additional calculated fields
    df['value_category'] = pd.cut(df['market_value'],
                                  bins=[0, 1000000, 2500000, 5000000, float('inf')],
                                  labels=['Small (<$1M)', 'Medium ($1-2.5M)', 'Large ($2.5-5M)', 'Very Large (>$5M)'])

    df['has_recent_trade'] = df['trade_type'].notna()

    # Save enhanced dataset for Power BI
    df.to_csv('powerbi/powerbi_dataset.csv', index=False)

    print("✓ Power BI dataset prepared with enhanced fields")
    print(f"  - Total records: {len(df)}")
    print(f"  - Value categories added: {df['value_category'].nunique()}")
    print(f"  - Trade activity flag added: {df['has_recent_trade'].sum()} portfolios with recent trades")

if __name__ == "__main__":
    print("=== Investment Data Processing Pipeline ===")
    print("Step 3-5: Report Generation and Visualization")

    try:
        # Generate Excel summaries
        client_summary, asset_summary = generate_excel_summary()

        # Create visualizations
        create_visualizations()

        # Prepare Power BI data
        generate_powerbi_data()

        print("\n🎉 All processing steps completed successfully!")
        print("\nGenerated Files:")
        print("- excel/client_portfolio_summary.csv")
        print("- excel/asset_class_summary.csv")
        print("- docs/portfolio_analysis_charts.png")
        print("- powerbi/powerbi_dataset.csv")

    except Exception as e:
        print(f"❌ Error during processing: {e}")