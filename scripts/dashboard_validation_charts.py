import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pandas_gbq

# NOTE: Ensure you are authenticated to Google Cloud (e.g., via `gcloud auth application-default login`
# or in a Colab environment using `from google.colab import auth; auth.authenticate_user()`)
# and PROJECT_ID is correctly set before running this script.
PROJECT_ID = 'driiiportfolio' # Replace with your actual GCP project ID
pandas_gbq.context.project = PROJECT_ID

def plot_avg_days_to_close_time_series():
    sql_avg_days_to_close_time_series = """
    SELECT
      FORMAT_DATE('%Y-%m', Intake_Date) AS month_year,
      AVG(Days_To_Close) AS avg_days_to_close
    FROM
      `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`
    GROUP BY
      month_year
    ORDER BY
      month_year;
    """
    df_avg_days_to_close = pandas_gbq.read_gbq(sql_avg_days_to_close_time_series, project_id=PROJECT_ID)
    df_avg_days_to_close['month_year'] = pd.to_datetime(df_avg_days_to_close['month_year'])

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='month_year', y='avg_days_to_close', data=df_avg_days_to_close)
    plt.title('Average Days to Close Over Time (Monthly)')
    plt.xlabel('Month-Year')
    plt.ylabel('Average Days to Close')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_regional_sla_bottlenecks():
    sql_regional_bottlenecks = """
    SELECT
      Region,
      pct_sla_breach
    FROM
      `driiiportfolio.tda_fns_compliance_analytics.executive_sla_performance`
    ORDER BY
      pct_sla_breach DESC;
    """
    df_regional_bottlenecks = pandas_gbq.read_gbq(sql_regional_bottlenecks, project_id=PROJECT_ID)

    plt.figure(figsize=(12, 6))
    sns.barplot(x='Region', y='pct_sla_breach', data=df_regional_bottlenecks, palette='viridis')
    plt.title('Regional SLA Breach Hotspots (Percentage of Breaches)')
    plt.xlabel('Region')
    plt.ylabel('Percentage SLA Breach (%)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_determination_friction():
    sql_determination_friction = """
    SELECT
      Determination,
      SLA_Breach,
      AVG(Days_To_Close) AS avg_days_to_close
    FROM
      `driiiportfolio.tda_fns_compliance_analytics.raw_complaint_pipeline`
    GROUP BY
      Determination, SLA_Breach
    ORDER BY
      Determination, SLA_Breach;
    """
    df_determination_friction = pandas_gbq.read_gbq(sql_determination_friction, project_id=PROJECT_ID)

    plt.figure(figsize=(12, 7))
    sns.barplot(x='Determination', y='avg_days_to_close', hue='SLA_Breach', data=df_determination_friction, palette='muted')
    plt.title('Average Resolution Time by Determination and SLA Breach Status')
    plt.xlabel('Determination')
    plt.ylabel('Average Days to Close')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.legend(title='SLA Breached')
    plt.tight_layout()
    plt.show()

def plot_civil_rights_outcomes():
    sql_civil_rights_outcomes = """
    SELECT
      Determination,
      civil_rights_cases_count
    FROM
      `driiiportfolio.tda_fns_compliance_analytics.civil_rights_determination_trajectory`
    ORDER BY
      civil_rights_cases_count DESC;
    """
    df_civil_rights_outcomes = pandas_gbq.read_gbq(sql_civil_rights_outcomes, project_id=PROJECT_ID)

    plt.figure(figsize=(8, 8))
    plt.pie(df_civil_rights_outcomes['civil_rights_cases_count'],
            labels=df_civil_rights_outcomes['Determination'],
            autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Civil Rights Cases by Determination Outcome')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def plot_civil_rights_monthly_trends():
    sql_civil_rights_monthly_trends = """
    SELECT
      month_year,
      total_civil_rights_cases,
      avg_days_to_close,
      pct_sla_breach
    FROM
      `driiiportfolio.tda_fns_compliance_analytics.civil_rights_timeline_trajectory`
    ORDER BY
      month_year;
    """

    df_civil_rights_trends = pandas_gbq.read_gbq(sql_civil_rights_monthly_trends, project_id=PROJECT_ID)
    df_civil_rights_trends['month_year'] = pd.to_datetime(df_civil_rights_trends['month_year'])

    fig, ax1 = plt.subplots(figsize=(14, 7))

    sns.lineplot(x='month_year', y='total_civil_rights_cases', data=df_civil_rights_trends, ax=ax1, color='blue', marker='o', label='Total Civil Rights Cases')
    ax1.set_xlabel('Month-Year')
    ax1.set_ylabel('Total Civil Rights Cases', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    sns.lineplot(x='month_year', y='avg_days_to_close', data=df_civil_rights_trends, ax=ax2, color='red', marker='x', linestyle='--', label='Avg Days to Close')
    sns.lineplot(x='month_year', y='pct_sla_breach', data=df_civil_rights_trends, ax=ax2, color='green', marker='s', linestyle=':', label='Pct SLA Breach (%)')

    ax2.set_ylabel('Average Days to Close / Pct SLA Breach (%)', color='black')
    ax2.tick_params(axis='y', labelcolor='black')

    plt.title('Civil Rights Cases: Monthly Trends (Volume, Resolution Time & SLA Breach)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    print("\n--- Plotting Average Days to Close Over Time ---")
    plot_avg_days_to_close_time_series()
    print("\n--- Plotting Regional SLA Bottlenecks ---")
    plot_regional_sla_bottlenecks()
    print("\n--- Plotting Determination Friction ---")
    plot_determination_friction()
    print("\n--- Plotting Civil Rights Case Outcomes ---")
    plot_civil_rights_outcomes()
    print("\n--- Plotting Civil Rights Cases: Monthly Trends ---")
    plot_civil_rights_monthly_trends()
