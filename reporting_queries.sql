-- Key reporting queries

-- 1. Portfolio summary by asset class
SELECT
    asset_class,
    COUNT(DISTINCT portfolio_id) as portfolio_count,
    SUM(market_value) as total_market_value,
    AVG(market_value) as avg_portfolio_value
FROM portfolio_data
GROUP BY asset_class
ORDER BY total_market_value DESC;

-- 2. Compliance status overview
SELECT
    compliance_status_standardized,
    COUNT(*) as portfolio_count,
    SUM(adjusted_market_value) as total_value
FROM consolidated_reporting
GROUP BY compliance_status_standardized;

-- 3. Trade activity summary
SELECT
    trade_type,
    COUNT(*) as trade_count,
    SUM(trade_amount) as total_amount,
    AVG(trade_amount) as avg_trade_size
FROM operations_data
WHERE status = 'Settled'
GROUP BY trade_type;

-- 4. Data quality check - portfolios without compliance
SELECT
    p.portfolio_id,
    p.client_id,
    p.market_value
FROM portfolio_data p
LEFT JOIN compliance_data c ON p.portfolio_id = c.portfolio_id
WHERE c.portfolio_id IS NULL;