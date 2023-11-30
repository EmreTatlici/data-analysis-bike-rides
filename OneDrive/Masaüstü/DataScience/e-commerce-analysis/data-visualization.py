# Data Visualization (Python)
# Import Necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the cleaned dataset
df_cleaned = pd.read_csv("cleaned_dataset.csv")

# Create the bar chart
fig = px.bar(
    df_cleaned,
    x='Age',
    y='Purchase Amount (USD)',
    color='Category',
    title='Column Chart of Purchases',
    labels={'Age': 'Customer Age', 'Purchase Amount (USD)': 'Purchase Amount'},
    category_orders={'Category': df_cleaned['Category'].unique()},  # Use unique values from the actual data
    hover_data=['Customer ID', 'Location', 'Purchase Amount (USD)']
)

# Customize the layout
fig.update_layout(
    showlegend=True,
    xaxis_title='Customer Age',
    yaxis_title='Purchase Amount',
    hovermode='closest'
)

# Show the plot
fig.show()