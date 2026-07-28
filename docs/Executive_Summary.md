# Executive Summary: TDA F&N Compliance Analytics Portfolio Project


**Complaint Resolution Investigator:** Daniel Rodriguez III

**Date:** July 27, 2026


## Project Objective

The primary objective of this portfolio project is to demonstrate an end-to-end analytical capability in compliance investigation. This involves simulating a complex case (Lone Star Independent School District), generating synthetic data reflecting a complaint pipeline, ingesting it into Google BigQuery, performing analytics engineering to identify operational bottlenecks and SLA breaches, and finally, visualizing these insights in a Looker Studio dashboard. The project concludes with strategic recommendations for process and software improvements.

## Demonstrated Competencies

This project meticulously showcases proficiency in:

### 1. Conducting Thorough Investigations
Through detailed case intake, evidence analysis, and statutory triangulation.

### 2. Interpreting and Applying Laws and Regulations
By referencing specific federal citations (7 CFR Part 15, 7 CFR Part 210, FNS Instruction 113-1) in substantiating findings.

### 3. Documenting and Reporting Findings
Exemplified by the **"Final Investigative Report"** which presents substantiated and inconclusive determinations.

### 4. Managing and Adhering to Strict SLAs
The project's core focus on the 30-day federal SLA and identifying factors contributing to breaches (like Civil Rights cases and non-responsive vendors).

### 5. Leveraging Data for Process Improvement
By generating and analyzing complaint data to identify systemic inefficiencies and propose actionable software and workflow enhancements (e.g., bifurcated case workflows, automated translation routing).

### 6. Collaborating with Program Advancement
By providing data-driven insights and recommendations to enhance operational efficiency and effectiveness.

## Case Study: Lone Star Independent School District (FNS-2026-0884)

The project simulates an investigation into the Lone Star Independent School District (LSISD) initiated on July 27, 2026, by the TDA Food & Nutrition (F&N) Division. Allegations included:

*   **Allegation A (Civil Rights):** Failure to provide federally mandated translated communication materials (Spanish menus and intake forms) for Limited English Proficiency (LEP) households, establishing discriminatory communication barriers.
*   **Allegation B (Programmatic/Financial):** Unauthorized diversion of National School Lunch Program (NSLP) federal reimbursements into the district's general fund account.

**Key Findings from Investigative Log:**
*   **Complainant Interview:** Parent reported lack of Spanish forms and menus, and an unanswered email to the principal regarding the deficiency.
*   **Respondent Interview:** LSISD Director of Child Nutrition Services admitted to a backorder on translated forms due to a vendor transition and claimed a financial transfer was an automated software error by EduLedger, for which audit logs were unavailable due to vendor non-responsiveness.

**Statutory Triangulation Matrix Highlights:**
*   **Allegation A (Civil Rights):** Probable Cause for Substantiation, citing 7 CFR § 15.3(b)(1) and FNS Instruction 113-1, confirmed by physical evidence and respondent admission.
*   **Allegation B (Financial):** Pending Data Dependency, citing 7 CFR § 210.14(a), due to lack of vendor audit logs from EduLedger to verify intent or software error.

## Resolution Approach: An End-to-End Analytical Pipeline

This project resolved the challenge of identifying and addressing systemic operational friction within compliance investigations through a robust, multi-phase analytical pipeline:

1.  **Data Generation:** An optimized Python script created a synthetic dataset of 250 compliance complaints, reflecting realistic operational scenarios and SLA metrics.
2.  **Cloud Ingestion & Data Quality:** This synthetic data was securely ingested into Google BigQuery. Rigorous SQL-based data quality checks confirmed data integrity, completeness, and adherence to defined logical anchors post-ingestion.
3.  **Analytics Engineering:** Three key analytical SQL views were engineered in BigQuery (`executive_sla_performance`, `non_responsive_bottleneck_analysis`, `civil_rights_determination_trajectory`, `civil_rights_timeline_trajectory`). These views aggregated data to expose critical operational friction points and SLA breach metrics.
4.  **Dashboard Development & Validation:** The engineered SQL views powered an interactive Looker Studio dashboard, providing executive visibility into compliance health. The dashboard's KPIs and visualizations were meticulously validated using Python and `pandas-gbq` within this notebook.

## Strategic Recommendations

Based on the insights derived from this data architecture, the following strategic recommendations are proposed to optimize TDA's complaint resolution process and improve SLA compliance:

1.  **Automated Escalation Trackers:** Implement automated alerts for cases approaching their SLA deadline, particularly those with a 'Non-Responsive' determination, to proactively notify investigators and supervisors.
2.  **Bifurcated Workflow Systems:** Enhance the tracking system (e.g., CAPPS/WIT) for multi-allegation complaints to allow independent sub-cases. This enables the timely closure of elements like Civil Rights findings within the 30-day mandate, while allowing other dependent allegations to proceed without artificially breaching the overall SLA. This directly addresses systemic delays observed in complex cases.

These data-driven recommendations aim to enhance operational efficiency, ensure adherence to federal mandates, and foster a more proactive approach to compliance management.
