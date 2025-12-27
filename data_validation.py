# Data Validation and Reconciliation Script
import pandas as pd
import numpy as np
from datetime import datetime

def load_data():
    """Load all datasets"""
    portfolio_df = pd.read_csv('data/raw/portfolio_data.csv')
    operations_df = pd.read_csv('data/raw/operations_data.csv')
    compliance_df = pd.read_csv('data/raw/compliance_data.csv')
    return portfolio_df, operations_df, compliance_df

def validate_portfolio_data(df):
    """Validate portfolio data"""
    print("=== Portfolio Data Validation ===")

    # Check for missing values
    missing_values = df.isnull().sum()
    print(f"Missing values:\n{missing_values}")

    # Check for negative market values
    negative_values = df[df['market_value'] < 0]
    if not negative_values.empty:
        print(f"Negative market values found:\n{negative_values}")
    else:
        print("✓ No negative market values")

    # Check date formats
    try:
        df['reporting_date'] = pd.to_datetime(df['reporting_date'])
        print("✓ Reporting dates are valid")
    except:
        print("✗ Invalid date formats in reporting_date")

    return df

def validate_operations_data(df):
    """Validate operations data"""
    print("\n=== Operations Data Validation ===")

    # Check for missing values
    missing_values = df.isnull().sum()
    print(f"Missing values:\n{missing_values}")

    # Check trade amounts
    negative_trades = df[df['amount'] < 0]
    if not negative_trades.empty:
        print(f"Negative trade amounts found:\n{negative_trades}")

    # Validate trade types
    valid_types = ['Buy', 'Sell']
    invalid_types = df[~df['trade_type'].isin(valid_types)]
    if not invalid_types.empty:
        print(f"Invalid trade types:\n{invalid_types}")
    else:
        print("✓ All trade types are valid")

    return df

def validate_compliance_data(df):
    """Validate compliance data"""
    print("\n=== Compliance Data Validation ===")

    # Check for missing values
    missing_values = df.isnull().sum()
    print(f"Missing values:\n{missing_values}")

    # Validate results
    valid_results = ['Pass', 'Fail']
    invalid_results = df[~df['result'].isin(valid_results)]
    if not invalid_results.empty:
        print(f"Invalid compliance results:\n{invalid_results}")
    else:
        print("✓ All compliance results are valid")

    return df

def reconcile_datasets(portfolio_df, operations_df, compliance_df):
    """Reconcile data across datasets"""
    print("\n=== Data Reconciliation ===")

    # Check portfolio coverage in operations
    portfolio_ids = set(portfolio_df['portfolio_id'])
    operations_portfolios = set(operations_df['portfolio_id'])
    missing_in_operations = portfolio_ids - operations_portfolios
    print(f"Portfolios without operations data: {missing_in_operations}")

    # Check portfolio coverage in compliance
    compliance_portfolios = set(compliance_df['portfolio_id'])
    missing_in_compliance = portfolio_ids - compliance_portfolios
    print(f"Portfolios without compliance data: {missing_in_compliance}")

    # Check for orphaned records
    orphaned_operations = operations_portfolios - portfolio_ids
    print(f"Operations for non-existent portfolios: {orphaned_operations}")

    orphaned_compliance = compliance_portfolios - portfolio_ids
    print(f"Compliance for non-existent portfolios: {orphaned_compliance}")

    return {
        'missing_operations': len(missing_in_operations),
        'missing_compliance': len(missing_in_compliance),
        'orphaned_operations': len(orphaned_operations),
        'orphaned_compliance': len(orphaned_compliance)
    }

def main():
    """Main validation function"""
    print("Starting Data Validation and Reconciliation...")

    # Load data
    portfolio_df, operations_df, compliance_df = load_data()

    # Validate each dataset
    portfolio_df = validate_portfolio_data(portfolio_df)
    operations_df = validate_operations_data(operations_df)
    compliance_df = validate_compliance_data(compliance_df)

    # Reconcile across datasets
    reconciliation_results = reconcile_datasets(portfolio_df, operations_df, compliance_df)

    print("\n=== Validation Summary ===")
    print(f"Total portfolios: {len(portfolio_df)}")
    print(f"Total operations: {len(operations_df)}")
    print(f"Total compliance checks: {len(compliance_df)}")
    print(f"Reconciliation issues: {sum(reconciliation_results.values())}")

    if sum(reconciliation_results.values()) == 0:
        print("✓ All data reconciliation checks passed")
    else:
        print("⚠ Data reconciliation issues found - review required")

if __name__ == "__main__":
    main()