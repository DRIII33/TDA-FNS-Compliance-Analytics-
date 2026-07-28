SELECT
  COUNT(*) AS total_records,
  COUNT(DISTINCT Complaint_ID) AS unique_complaint_ids,
  COUNTIF(Complaint_ID IS NULL OR TRIM(Complaint_ID) = '') AS blank_or_null_ids,
  COUNT(*) - COUNT(DISTINCT Complaint_ID) AS total_duplicate_rows
FROM
  `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`;
