content:
import pandas as pd
import pandas_gbq

# NOTE: Ensure you are authenticated to Google Cloud (e.g., via `gcloud auth application-default login`
# or in a Colab environment using `from google.colab import auth; auth.authenticate_user()`)
# and PROJECT_ID is correctly set before running this script.
PROJECT_ID = 'driiiportfolio' # Replace with your actual GCP project ID
pandas_gbq.context.project = PROJECT_ID

def get_overall_sla_breach_rate():
    sql_kpi_sla_breach = """
    SELECT
      ROUND(COUNTIF(SLA_Breach IS TRUE) * 100 / COUNT(*), 2) AS overall_pct_sla_breach
    FROM
      `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`;
    """
    df_overall_sla_breach = pandas_gbq.read_gbq(sql_kpi_sla_breach, project_id=PROJECT_ID)
    overall_sla_breach_rate = df_overall_sla_breach['overall_pct_sla_breach'].iloc[0]
    return overall_sla_breach_rate

if __name__ == '__main__':
    sla_rate = get_overall_sla_breach_rate()
    print(f"Overall SLA Breach Rate: {sla_rate:.2f}%")
