SELECT
  Program_Type,
  COUNT(*) AS volume,
  ROUND(COUNT(*) * 100 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`
GROUP BY Program_Type ORDER BY volume DESC;
