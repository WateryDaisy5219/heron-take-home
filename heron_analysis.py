## import statements
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from scipy import stats
import numpy as np

def plot_metrics(df):
    specific_metric = 'merchant_coverage'
    metric_data = df[df['metric_label'] == specific_metric]
    print(f"Statistics for {specific_metric}:")
    print(metric_data['metric_value'].describe())
    metric_data.hist()
    plt.show()

def normalize_heron_score(value):
    if pd.notna(value):  # Check if the value is not NaN
        if 0 <= value <= 1:
            return value * 1000
        else:
            return value
    return value

def create_correlation(df):
    # Create a pivot table with heron_id as index and metrics as columns
    pivot_df = df.pivot_table(
        index='heron_id', 
        columns='metric_label', 
        values='metric_value',
        aggfunc='first'  # Use 'first' if you have one value per heron/metric
    )

    # Reset index to make heron_id a regular column
    pivot_df = pivot_df.reset_index()

    # Calculate correlation with heron_score
    correlations = {}
    p_values = {}
    heron_score_column = pivot_df['heron_score']

    # Loop through all columns except heron_score and heron_id
    for column in pivot_df.columns:
        if column not in ['heron_score', 'heron_id']:
            # Remove rows where either value is NaN
            valid_data = pd.concat([pivot_df[column], heron_score_column], axis=1).dropna()
            
            if len(valid_data) > 1:  # Need at least 2 points for correlation
                correlation, p_value = pearsonr(valid_data[column], valid_data['heron_score'])
                correlations[column] = correlation
                p_values[column] = p_value

    # Convert to DataFrame for easier viewing
    correlation_df = pd.DataFrame({
        'Metric': correlations.keys(),
        'Correlation with heron_score': correlations.values(),
        'P-Value': p_values.values()
    })

    # Sort by absolute correlation value (strongest relationships first)
    correlation_df['Abs Correlation'] = correlation_df['Correlation with heron_score'].abs()
    correlation_df = correlation_df.sort_values('Abs Correlation', ascending=False).drop('Abs Correlation', axis=1)

    print("Correlations with heron_score:")
    print(correlation_df)

    # Visualize top correlations
    top_metrics = correlation_df.head(10)['Metric'].tolist()

    # Create a bar chart of correlations
    plt.figure(figsize=(12, 8))
    plt.barh(top_metrics, correlation_df.head(10)['Correlation with heron_score'])
    plt.xlabel('Correlation with heron_score')
    plt.ylabel('Metric')
    plt.title('Top 10 Metrics Correlated with heron_score')
    plt.axvline(x=0, color='black', linestyle='-', alpha=0.3)
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Create scatter plots for top 5 correlated metrics
    fig, axes = plt.subplots(3, 2, figsize=(15, 15))
    axes = axes.flatten()

    for i, metric in enumerate(top_metrics[:5]):
        sns.scatterplot(
            x=pivot_df[metric], 
            y=pivot_df['heron_score'],
            ax=axes[i]
        )
        axes[i].set_title(f'heron_score vs {metric} (r={correlations[metric]:.2f})')
        axes[i].set_xlabel(metric)
        axes[i].set_ylabel('heron_score')
        
        # Add regression line
        sns.regplot(
            x=pivot_df[metric], 
            y=pivot_df['heron_score'],
            scatter=False,
            ax=axes[i],
            line_kws={"color":"red"}
        )

    # If we only used 5 plots, disable the 6th subplot
    if len(top_metrics) < 6:
        axes[5].axis('off')
        
    plt.tight_layout()
    plt.show()

def analysis_to_csv(df):
    # Create a pivot table for correlation analysis

    heron_score_label = 'heron_score'
    pivot_df = df.pivot_table(
        index='heron_id', 
        columns='metric_label', 
        values='metric_value',
        aggfunc='first'
    )

    # Create a list to store our analytics results
    metrics_analysis = []

    # List of metric labels (using the ones you provided)
    metric_labels = [
        'inflow_growth_rate', 'inflow_daily_average', 'outflow_daily_average', 
        'latest_balance', 'balance_minimum', 'balance_average', 'change_in_balance', 
        'weekday_balance_average', 'weekday_with_highest_avg', 'weekday_with_lowest_avg', 
        'data_volume', 'date_range', 'data_freshness', 'has_balance_ratio', 
        'data_coverage', 'accounts', 'potentially_duplicated_account_pairs', 
        'inflows', 'outflows', 'inflow_amount', 'confidence', 'revenue_anomalies', 
        'last_debt_investment', 'last_debt_investment_days', 'debt_repayment_daily_average', 
        'debt_investment', 'debt_investors', 'debt_investment_count', 'debt_repayment', 
        'debt_service_coverage_ratio', 'merchant_heron_ids', 'predicted_nsf_fees', 
        'predicted_balance_daily_average', 'heron_score', 'category_coverage', 
        'merchant_coverage', 'unconnected_account_ratio', 'revenue_daily_average', 
        'cogs_daily_average', 'opex_daily_average', 'revenue_sources', 'revenue', 
        'annualized_revenue', 'cogs', 'average_credit_card_spend', 'opex', 
        'revenue_profit_and_loss', 'annualized_revenue_profit_and_loss', 
        'cogs_profit_and_loss', 'opex_profit_and_loss', 'revenue_monthly_average', 
        'revenue_growth_rate', 'gross_operating_cashflow_daily_average', 
        'net_operating_cashflow_daily_average', 'gross_operating_cashflow', 
        'net_operating_cashflow', 'gross_operating_cashflow_profit_and_loss', 
        'net_operating_cashflow_profit_and_loss', 'deposit_days', 'nsf_fees', 
        'nsf_days', 'debt_collection', 'atm_withdrawals', 'tax_payments', 
        'tax_payment_amount', 'negative_balance_days', 'negative_balance_days_by_account', 
        'distinct_mcas_from_outflows', 'distinct_mcas_from_inflows'
    ]

    # Ensure these metrics actually exist in your data
    actual_metrics = df['metric_label'].unique()

    # Calculate correlation with Heron Score if it exists in the pivot table
    has_heron_score = heron_score_label in pivot_df.columns

    # Analyze each metric
    for metric in actual_metrics:
        # Get data for this metric
        metric_data = df[df['metric_label'] == metric]['metric_value'].dropna()
        
        if len(metric_data) == 0:
            print(f"Warning: No data found for metric {metric}")
            continue
        
        # Calculate basic statistics
        count = len(metric_data)
        avg = metric_data.mean()
        median = metric_data.median()
        min_val = metric_data.min()
        max_val = metric_data.max()
        std_dev = metric_data.std()
        
        # Calculate percentiles
        p10 = metric_data.quantile(0.1)
        p25 = metric_data.quantile(0.25)
        p75 = metric_data.quantile(0.75)
        p90 = metric_data.quantile(0.9)
        
        # Calculate correlation with Heron Score if both exist in pivot table
        correlation = np.nan
        p_value = np.nan
        
        if has_heron_score and metric in pivot_df.columns:
            # Get data for correlation calculation
            both_data = pivot_df[[metric, heron_score_label]].dropna()
            
            if len(both_data) >= 2:  # Need at least 2 points for correlation
                correlation, p_value = stats.pearsonr(
                    both_data[metric], 
                    both_data[heron_score_label]
                )
        
        # Store the results
        metrics_analysis.append({
            'Metric': metric,
            'Count': count,
            'Average': avg,
            'Median': median,
            'Min': min_val,
            'Max': max_val,
            'StdDev': std_dev,
            'P10': p10,
            'P25': p25,
            'P75': p75,
            'P90': p90,
            'Correlation_with_Heron_Score': correlation,
            'P_Value': p_value
        })

    # Convert to DataFrame
    metrics_df = pd.DataFrame(metrics_analysis)

    # print(metrics_df)
    # raise 'w'

    # # Sort by absolute correlation with Heron Score (if available)
    # if has_heron_score:
    #     metrics_df['Abs_Correlation'] = metrics_df['Correlation_with_Heron_Score'].apply(
    #     lambda x: abs(x) if not pd.isna(x) else 0
    # )
    #     metrics_df = metrics_df.sort_values('Abs_Correlation', ascending=False)
    #     metrics_df = metrics_df.drop('Abs_Correlation', axis=1)

    # Save to CSV
    metrics_df.to_csv('metrics_analysis.csv', index=False)
    print(f"Analysis complete. Results saved to metrics_analysis.csv")

def main():
    ## read csv into dataframe
    df = pd.read_csv('company_metrics.csv')
    # print(df.describe())

    ## normalize heron_score to 1-1000 scale
    heron_score_data = df[df['metric_label'] == 'heron_score'].copy()
    heron_score_data['normalized_score'] = heron_score_data['metric_value'].apply(normalize_heron_score)
    df.loc[df['metric_label'] == 'heron_score', 'metric_value'] = heron_score_data['normalized_score']

    return df


if __name__ == "__main__":
    dataframe = main()
    # create_correlation(dataframe)
    # plot_metrics(dataframe)
    analysis_to_csv(dataframe)
