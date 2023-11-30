# Data Exploration (Python)
# Import Necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("shopping_behavior_updated.csv")

# Display the first rows of the Dataset
print("First few rows of the dataset:")
print(df.head())

# Basic information about the dataset
print("\nDataset Information:")
print(df.info())

# Summary statistics of numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for duplicates
print("\nDuplicate Rows:")
print(df[df.duplicated()])

# Unique values in categorical columns
print("\nUnique Values in Categorical Columns:")
for col in df.select_dtypes(include='object').columns:
    print(f"{col}: {df[col].unique()}")


# Visualize data distribution for numerical columns (using matplotlib)
df.hist(figsize=(12, 10), bins=20)
plt.suptitle("Histograms of Numerical Columns")
plt.show()