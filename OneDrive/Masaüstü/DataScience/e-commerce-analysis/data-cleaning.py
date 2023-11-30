# Data Cleaning (Python)
# Import Necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("shopping_behavior_updated.csv")
# Handling Missing Values
# Drop rows with missing values
df_cleaned = df.dropna()

# Alternatively, fill missing values with a specific value or the mean/median
# df_cleaned = df.fillna(value_or_method)

# Handling Duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Convert Data Types if Necessary
# Check data types of each column
print("Data Types Before Conversion:")
print(df_cleaned.dtypes)
# Convert specific columns to the desired data type (if needed)
# df_cleaned['column_name'] = df_cleaned['column_name'].astype('desired_data_type')

# Check for any remaining missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df_cleaned.isnull().sum())

# Check for any remaining duplicates after cleaning
print("\nDuplicate Rows After Cleaning:")
print(df_cleaned[df_cleaned.duplicated()])

# Summary statistics of cleaned data
print("\nSummary Statistics of Cleaned Data:")
print(df_cleaned.describe())

# Save the cleaned dataset to a new CSV file
df_cleaned.to_csv(r"C:\Users\emre-\OneDrive\Masaüstü\DataScience\e-commerce-analysis\cleaned_dataset.csv", index=False)
