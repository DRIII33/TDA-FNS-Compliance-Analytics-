CREATE OR REPLACE VIEW `driiiportfolio.tda_fns_compliance_analytics.executive_sla_performance` AS
SELECT
  Region,
  Program_Type,
  COUNT(*) AS total_cases,
  AVG(Days_To_Close) AS avg_days_to_close,
  ROUND(COUNTIF(SLA_Breach IS TRUE) * 100 / COUNT(*), 2) AS pct_sla_breach
FROM
  `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`
GROUP BY
  Region, Program_Type
ORDER BY
  Region, Program_Type;
