CREATE OR REPLACE VIEW `driiiportfolio.tda_fns_compliance_analytics.civil_rights_timeline_trajectory` AS
SELECT
  FORMAT_DATE('%Y-%m', Intake_Date) AS month_year,
  COUNT(*) AS total_civil_rights_cases,
  AVG(Days_To_Close) AS avg_days_to_close,
  ROUND(COUNTIF(SLA_Breach IS TRUE) * 100 / COUNT(*), 2) AS pct_sla_breach
FROM
  `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`
WHERE
  Civil_Rights_Flag IS TRUE
GROUP BY
  month_year
ORDER BY
  month_year;
