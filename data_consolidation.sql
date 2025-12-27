-- Consolidated reporting view
-- Joins all three datasets for comprehensive reporting

CREATE OR REPLACE VIEW consolidated_reporting AS
SELECT
    p.portfolio_id,
    p.client_id,
    p.asset_class,
    p.market_value,
    p.reporting_date as portfolio_date,
    o.trade_id,
    o.trade_type,
    o.amount as trade_amount,
    o.settlement_date,
    o.status as trade_status,
    c.compliance_id,
    c.rule_type,
    c.check_date,
    c.result as compliance_result,
    c.notes as compliance_notes,
    -- Standardized columns for reporting
    CASE
        WHEN c.result = 'Pass' THEN 'Compliant'
        WHEN c.result = 'Fail' THEN 'Non-Compliant'
        ELSE 'Pending'
    END as compliance_status_standardized,
    -- Calculated fields
    p.market_value + COALESCE(o.amount, 0) as adjusted_market_value
FROM portfolio_data p
LEFT JOIN operations_data o ON p.portfolio_id = o.portfolio_id
LEFT JOIN compliance_data c ON p.portfolio_id = c.portfolio_id
WHERE p.reporting_date >= '2023-01-01'
ORDER BY p.portfolio_id, p.reporting_date DESC;