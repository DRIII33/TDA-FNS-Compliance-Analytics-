import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_tda_fns_pipeline_data_optimized(num_records=250):
    """
    Generates a high-fidelity, legally aligned synthetic dataset representing
    the Texas Department of Agriculture (TDA) Food & Nutrition case pipeline.

    Fixes logical paradoxes by binding operational timelines to case complexity.
    """
    # Fix the random seed for reproducible, audit-ready data generation
    np.random.seed(42)

    # Establish structural anchors matching TDA State Job Code 1354 parameters
    program_types = ['NSLP', 'CACFP', 'SFSP']
    regions = ['Austin', 'Houston', 'Dallas', 'Lubbock', 'San Antonio', 'Fort Worth']
    determinations_pool = ['Substantiated', 'Unsubstantiated', 'Inconclusive', 'Non-Responsive']

    complaint_ids = [f"FNS-2025-{str(i).zfill(4)}" for i in range(1, num_records + 1)]

    # Map timelines directly to a single standard Texas State Fiscal Year (FY25/26)
    start_date = datetime(2025, 7, 1)
    end_date = datetime(2026, 6, 30)
    days_between = (end_date - start_date).days
    random_days = np.random.randint(0, days_between, size=num_records)
    intake_dates = [(start_date + timedelta(days=int(d))).strftime('%Y-%m-%d') for d in random_days]

    # Establish base tracking arrays
    civil_rights_flags = np.random.choice([True, False], size=num_records, p=[0.3, 0.7])
    programs = np.random.choice(program_types, size=num_records)
    regions_selected = np.random.choice(regions, size=num_records)

    determinations_selected = []
    days_to_close = []

    # Interwoven logic block binding operational complexity to statutory realities
    for flag in civil_rights_flags:
        if flag:
            # Civil Rights cases skew toward Substantiated/Inconclusive due to rigorous federal thresholds
            det = np.random.choice(determinations_pool, p=[0.5, 0.2, 0.2, 0.1])

            # Inter-agency routing bottlenecks add standard baseline administrative delay
            if det == 'Non-Responsive':
                days = int(np.random.normal(38, 4)) # Compounded delay: Federal routing + vendor resistance
            else:
                days = int(np.random.normal(35, 7)) # Standalone multi-tiered civil rights processing time
        else:
            # Standard programmatic cases (e.g., routine meal pattern compliance)
            det = np.random.choice(determinations_pool, p=[0.35, 0.4, 0.15, 0.1])

            if det == 'Non-Responsive':
                days = int(np.random.normal(33, 4)) # Structural delay driven purely by vendor resistance
            else:
                days = int(np.random.normal(20, 5)) # Routine administrative workflow moving efficiently

        # Enforce an absolute logical operational minimum of 5 days for intake/triage processing
        days = max(5, days)
        determinations_selected.append(det)
        days_to_close.append(days)

    # Strictly define SLA Breach based on the federal 30-day mandate
    sla_breaches = [True if d > 30 else False for d in days_to_close]

    # Construct clean, structured DataFrame
    df = pd.DataFrame({
        'Complaint_ID': complaint_ids,
        'Intake_Date': intake_dates,
        'Days_To_Close': days_to_close,
        'Program_Type': programs,
        'Civil_Rights_Flag': civil_rights_flags,
        'Determination': determinations_selected,
        'Region': regions_selected,
        'SLA_Breach': sla_breaches
    })

    return df

if __name__ == '__main__':
    tda_dataset = generate_tda_fns_pipeline_data_optimized(250)
    tda_dataset.to_csv('data/tda_fns_complaint_pipeline_optimized.csv', index=False)
    print("SUCCESS: Optimized compliance dataset saved to 'data/tda_fns_complaint_pipeline_optimized.csv'.")
    print("You may also want to print tda_dataset.info() and tda_dataset.head() for validation.")
