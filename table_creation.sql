-- Create portfolio data table
CREATE OR REPLACE TABLE portfolio_data (
    portfolio_id VARCHAR(10),
    client_id VARCHAR(10),
    asset_class VARCHAR(50),
    market_value DECIMAL(15,2),
    reporting_date DATE
);

-- Create operations data table
CREATE OR REPLACE TABLE operations_data (
    trade_id VARCHAR(10),
    portfolio_id VARCHAR(10),
    trade_type VARCHAR(10),
    amount DECIMAL(15,2),
    settlement_date DATE,
    status VARCHAR(20)
);

-- Create compliance data table
CREATE OR REPLACE TABLE compliance_data (
    compliance_id VARCHAR(10),
    portfolio_id VARCHAR(10),
    rule_type VARCHAR(50),
    check_date DATE,
    result VARCHAR(10),
    notes VARCHAR(255)
);