# Dashboard Executive Summary: TDA F&N Compliance Analytics


**Complaint Resolution Investigator:** Daniel Rodriguez III

**Date:** July 27, 2026


This document provides a detailed overview and analysis of the TDA F&N Compliance Analytics Looker Studio Dashboard, which was developed to provide executive stakeholders with clear, actionable insights into the agency's operational efficiency and adherence to the 30-day federal Service Level Agreement (SLA). The dashboard translates complex analytical engineering into an intuitive visual narrative, highlighting key performance indicators and operational friction points.

## Dashboard Architecture and Key Insights

The dashboard is structured into two main pages: an "Executive Overview: SLA Performance & Bottlenecks" and a "Deep Dive: Civil Rights Caseload & Resolution Trends," each designed to address specific aspects of compliance monitoring.

### Page 1: Executive Overview: SLA Performance & Bottlenecks

This page provides a high-level view of the agency's compliance health, identifying areas of concern at a glance.

#### 1. KPI Scorecard: Overall SLA Breach Rate
*   **Purpose:** Provides immediate visibility into the agency's overall compliance with the 30-day federal mandate.
*   **Insight:** The dashboard prominently displays the **Overall SLA Breach Rate, calculated at 25.60%**. This critical metric immediately flags that a significant portion of cases are exceeding the federal mandate, necessitating further investigation.

#### 2. Time Series Line Chart: Average Resolution Time
*   **Purpose:** Tracks operational efficiency trends by visualizing the average `Days_To_Close` over time.
*   **Insight:** The "Average Days to Close Over Time (Monthly)" chart reveals fluctuations in resolution times across months. It allows for the identification of periods of increased operational burden or improved efficiency, offering a temporal perspective on case processing. For instance, initial months might show higher resolution times, settling into a pattern later, or exhibiting seasonal peaks.

#### 3. Regional Bottlenecks: Regional SLA Breach Hotspots (Geo Chart / Bar Chart)
*   **Purpose:** Identifies geographical regions that disproportionately contribute to SLA breaches, enabling targeted resource allocation.
*   **Insight:** Represented by a bar chart in our validation (simulating a Looker Studio Geo Chart), the "Regional SLA Breach Hotspots" clearly indicates that **Austin and Fort Worth exhibit the highest percentages of SLA breaches**. This pinpoints specific field offices requiring immediate attention, process review, or additional support to improve compliance.

#### 4. Stacked Bar Chart: Determination Friction
*   **Purpose:** Illustrates how different case determination types (e.g., Substantiated, Non-Responsive) and their `SLA_Breach` status impact resolution times.
*   **Insight:** The "Average Resolution Time by Determination and SLA Breach Status" chart graphically demonstrates that cases resulting in an `SLA_Breach = TRUE` consistently have higher average `Days_To_Close` across all determination types. Notably, **'Unsubstantiated' cases, when breached, show the longest resolution times**, followed closely by 'Non-Responsive' and 'Substantiated' breached cases. This visual emphasizes that specific determination outcomes are inherently more prone to delays, especially when they exceed the SLA.

### Page 2: Deep Dive: Civil Rights Caseload & Resolution Trends

This page offers a focused analysis on high-risk Civil Rights cases, which are often complex and sensitive.

#### 5. Pie Chart: Civil Rights Case Outcomes
*   **Purpose:** Shows the distribution of determination outcomes specifically for Civil Rights cases, providing insight into their typical resolution paths.
*   **Insight:** The "Civil Rights Cases by Determination Outcome" pie chart highlights that **half (50.0%) of all Civil Rights cases are substantiated**, while approximately a fifth each are unsubstantiated (21.4%) or inconclusive (18.6%). This distribution helps understand the inherent complexity and often clear-cut nature of Civil Rights violations within the dataset.

#### 6. Line Chart: Civil Rights Cases: Monthly Trends
*   **Purpose:** Visualizes the monthly trends for Civil Rights cases, including volume, average days to close, and percentage of SLA breaches, to track their trajectory and impact.
*   **Insight:** The "Civil Rights Cases: Monthly Trends (Volume, Resolution Time & SLA Breach)" multi-axis line chart allows for a comprehensive temporal analysis. It shows how the volume of Civil Rights cases, their average `Days_To_Close`, and `Pct SLA Breach` vary monthly. This helps identify periods of higher caseloads for Civil Rights complaints and corresponding impacts on resolution speed or SLA compliance, enabling proactive resource planning and intervention. For example, spikes in `Pct SLA Breach` might correlate with increased case volume or particular months, revealing systemic issues.

## General Dashboard Elements

Beyond the core charts, the dashboard incorporates essential interactive elements to empower users:
*   **Date Range Control:** Allows users to filter data by specific time periods, enabling historical analysis and trend identification.
*   **Filter Controls:** Drop-down filters for `Region`, `Program_Type`, `Civil_Rights_Flag`, and `Determination` enable granular data exploration, allowing stakeholders to drill down into specific operational silos and customize their view of the data.

## Conclusion

The TDA F&N Compliance Analytics Dashboard provides a comprehensive, interactive platform for monitoring and understanding the dynamics of compliance investigations. By clearly presenting critical KPIs, identifying regional and determination-specific bottlenecks, and offering a deep dive into Civil Rights cases, the dashboard serves as a vital tool for data-driven decision-making, ultimately contributing to improved operational efficiency and enhanced adherence to federal mandates.
