import pandas as pd
import numpy as np

# Create a DataFrame with sample data
data = {
    'Age': [25, 45, 35, 32, 40, 50, 48, 20],
    'Salary': [50000, 80000, 60000, 62000, 70000, 90000, 82000, 30000],
    'Years_at_Company': [1, 10, 8, 4, 7, 12, 11, 1]
}

df = pd.DataFrame(data)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Display the correlation matrix
print(correlation_matrix)
