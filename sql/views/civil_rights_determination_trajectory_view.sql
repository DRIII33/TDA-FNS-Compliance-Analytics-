CREATE OR REPLACE VIEW `driiiportfolio.tda_fns_compliance_analytics.civil_rights_determination_trajectory` AS
SELECT
  Determination,
  COUNT(*) AS civil_rights_cases_count,
  ROUND(COUNT(*) * 100 / (SELECT COUNT(*) FROM `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline` WHERE Civil_Rights_Flag IS TRUE), 2) AS pct_of_civil_rights_cases,
  AVG(Days_To_Close) AS avg_days_to_close_civil_rights
FROM
  `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`
WHERE
  Civil_Rights_Flag IS TRUE
GROUP BY
  Determination
ORDER BY
  civil_rights_cases_count DESC;
