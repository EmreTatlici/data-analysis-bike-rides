# Data Analysis (Python)
# Import Necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the cleaned dataset
df = pd.read_csv("cleaned_dataset.csv")

# Descriptive Statistics
# Display summary statistics for numerical columns
print("Summary Statistics:")
print(df.describe())


# Analyze Customer Purchasing Patterns
# Group by customer and calculate average purchase amount and frequency
customer_stats = df.groupby('Customer ID').agg({
    'Purchase Amount (USD)': ['mean', 'sum'],
    'Frequency of Purchases': 'count'
}).reset_index()

# Rename columns for clarity
customer_stats.columns = ['Customer ID', 'Avg Purchase Amount', 'Total Purchase Amount', 'Purchase Frequency']

# Display the top 10 customers by total purchase amount
print("\nTop 10 Customers by Total Purchase Amount:")
print(customer_stats.sort_values(by='Total Purchase Amount', ascending=False).head(10))

# Explore Correlations Between Numerical Variables
numerical_columns = df.select_dtypes(include=['number']).columns
correlation_matrix = df[numerical_columns].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)




# Data Visualization
# Pairplot for numerical variables
sns.pairplot(df[numerical_columns])
plt.show()

# Boxplot for purchase amount by category
plt.figure(figsize=(12, 8))
sns.boxplot(x='Category', y='Purchase Amount (USD)', data=df)
plt.title('Purchase Amount Distribution by Category')
plt.show()