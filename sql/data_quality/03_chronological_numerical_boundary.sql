SELECT
  MIN(Intake_Date) AS earliest_intake_date,
  MAX(Intake_Date) AS latest_intake_date,
  COUNTIF(Intake_Date > CURRENT_DATE()) AS future_intake_dates,

  MIN(Days_To_Close) AS min_days_to_close,
  MAX(Days_To_Close) AS max_days_to_close,
  AVG(Days_To_Close) AS avg_days_to_close,
  COUNTIF(Days_To_Close < 0) AS negative_days_to_close
FROM
  `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`;
