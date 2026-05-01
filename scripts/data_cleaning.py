import pandas as pd 
import numpy as np

# Show all columns
pd.set_option('display.max_columns', None)

# Load dataset
df = pd.read_csv("/content/HR_Analytics.csv")

# Initial inspection
df.shape
df.columns
df.info()
df.describe()

# Rename columns for consistency and readability
df.columns = [
    'emp_id',
    'age',
    'age_group',
    'attrition',
    'business_travel',
    'daily_rate',
    'department',
    'distance_from_home_km',
    'education',
    'education_field',
    'employee_count',
    'employee_number',
    'environment_satisfaction',
    'gender',
    'job_involvement',
    'job_level',
    'job_role',
    'job_satisfaction',
    'marital_status',
    'monthly_income',
    'salary_slab',
    'hourly_rate',
    'num_companies_worked',
    'over_18',
    'over_time',
    'salary_hike_percent',
    'performance_rating',
    'relationship_satisfaction',
    'standard_working_hours',
    'stock_option_level',
    'total_experience_years',
    'trainings_last_year',
    'work_life_balance',
    'years_at_company',
    'years_in_current_role',
    'years_since_promotion',
    'years_with_curr_manager'
]

# Check and remove duplicates
df.duplicated().sum()
df = df.drop_duplicates()

# Check missing values
df.isnull().sum()

# Only a small percentage of values are missing (~4%)
# Use median imputation to handle missing values in numeric column
df['years_with_curr_manager'] = df['years_with_curr_manager'].fillna(
    df['years_with_curr_manager'].median()
)

# Analyze attrition by department (percentage)
pd.crosstab(df['attrition'], df['department'], normalize='columns') * 100

# Standardize categorical values: convert to lowercase and replace '-' with '_' to maintain consistency
df['business_travel'] = df['business_travel'].str.replace("-", "_").str.lower()

# Save the cleaned dataset to a new CSV file
df.to_csv("HR_Analytics.csv", index=False)

