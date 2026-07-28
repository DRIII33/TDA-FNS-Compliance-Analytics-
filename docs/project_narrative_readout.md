## Project Narrative & Readout Summary


**Complaint Resolution Investigator:** Daniel Rodriguez III

**Date:** July 27, 2026


### The Problem Statement

The TDA Food & Nutrition division faced significant operational friction, leading to systemic breaches of the federal 30-day SLA. Our analysis confirmed that complex Civil Rights cases and the non-responsiveness of sub-recipients were primary drivers of these delays.

Specifically, the overall SLA breach rate was 25.60%. Cases involving "Non-Responsive" determinations often exceeded the 30-day target, especially for Civil Rights-flagged cases (Avg. Days to Close for Civil Rights and Non-Responsive: 37.43 days).

### The Data Solution

To address this, we engineered a comprehensive synthetic data pipeline:

1.  **Synthetic Data Generation (Python):** Created a high-fidelity dataset simulating the TDA complaint pipeline, embedding realistic operational friction points and SLA breaches.

2.  **Cloud Ingestion & Warehousing (BigQuery):** Securely ingested this data into a scalable BigQuery environment (`driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`) after rigorous data quality checks.

3.  **Analytics Engineering (SQL Views):** Developed analytical views (`executive_sla_performance`, `non_responsive_bottleneck_analysis`, `civil_rights_determination_trajectory`, `civil_rights_timeline_trajectory`) to surface key performance indicators, regional bottlenecks, and civil rights caseload trends. These views directly powered an interactive Looker Studio dashboard.

### The Strategic Recommendation

Based on the insights derived from this data architecture, we recommend the implementation of:
1.  **Automated Escalation Trackers:** For cases approaching their SLA deadline, particularly those with a 'Non-Responsive' determination, automated alerts should notify investigators and supervisors.
2.  **Bifurcated Workflow Systems:** For multi-allegation complaints, the tracking system (e.g., CAPPS/WIT) should be enhanced to allow independent sub-cases. This enables the closure of elements like Civil Rights findings within the 30-day mandate, while allowing other dependent allegations to proceed without artificially breaching the overall SLA. This directly addresses the systemic delays observed in Civil Rights cases (Average days to close for Civil Rights cases: 34.26 days).

These data-driven recommendations aim to optimize TDA's complaint resolution process, improve SLA compliance, and enhance overall operational efficiency.
