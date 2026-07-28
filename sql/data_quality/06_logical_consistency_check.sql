SELECT
  COUNTIF(Days_To_Close > 30 AND SLA_Breach IS FALSE) AS suspected_unflagged_breaches,
  COUNTIF(Days_To_Close <= 30 AND SLA_Breach IS TRUE) AS suspected_false_breaches
FROM
  `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`;
