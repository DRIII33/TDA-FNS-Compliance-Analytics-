CREATE OR REPLACE VIEW `driiiportfolio.tda_fns_compliance_analytics.non_responsive_bottleneck_analysis` AS
SELECT
  Civil_Rights_Flag,
  COUNT(*) AS total_non_responsive_cases,
  AVG(Days_To_Close) AS avg_days_to_close_non_responsive,
  ROUND(COUNTIF(SLA_Breach IS TRUE) * 100 / COUNT(*), 2) AS pct_sla_breach_non_responsive
FROM
  `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`
WHERE
  Determination = 'Non-Responsive'
GROUP BY
  Civil_Rights_Flag
ORDER BY
  Civil_Rights_Flag;
