-- Sample SQL query for data consolidation
SELECT 
    portfolio_id,
    client_id,
    investment_amount,
    compliance_status,
    reporting_date
FROM investment_data
JOIN operations_data ON investment_data.id = operations_data.investment_id
WHERE reporting_date >= '2023-01-01';