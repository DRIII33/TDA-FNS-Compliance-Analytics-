SELECT
  Civil_Rights_Flag,
  SLA_Breach,
  COUNT(*) AS combination_count
FROM
  `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`
GROUP BY
  Civil_Rights_Flag,
  SLA_Breach;
