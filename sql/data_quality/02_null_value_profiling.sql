SELECT
  COUNT(*) AS total_rows,

  -- Counts
  COUNTIF(Intake_Date IS NULL) AS null_Intake_Date,
  COUNTIF(Days_To_Close IS NULL) AS null_Days_To_Close,
  COUNTIF(Program_Type IS NULL OR TRIM(Program_Type) = '') AS null_or_empty_Program_Type,
  COUNTIF(Civil_Rights_Flag IS NULL) AS null_Civil_Rights_Flag,
  COUNTIF(Determination IS NULL OR TRIM(Determination) = '') AS null_or_empty_Determination,
  COUNTIF(Region IS NULL OR TRIM(Region) = '') AS null_or_empty_Region,
  COUNTIF(SLA_Breach IS NULL) AS null_SLA_Breach,

  -- Percentages
  ROUND(COUNTIF(Intake_Date IS NULL) * 100 / COUNT(*), 2) AS pct_null_Intake_Date,
  ROUND(COUNTIF(Days_To_Close IS NULL) * 100 / COUNT(*), 2) AS pct_null_Days_To_Close,
  ROUND(COUNTIF(Program_Type IS NULL OR TRIM(Program_Type) = '') * 100 / COUNT(*), 2) AS pct_null_Program_Type,
  ROUND(COUNTIF(Region IS NULL OR TRIM(Region) = '') * 100 / COUNT(*), 2) AS pct_null_Region
FROM
  `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`;
