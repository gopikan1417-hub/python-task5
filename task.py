import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("Sample - Superstore 31.07.2026.csv", encoding="latin1")
# Display the first 5 rows
print(df.head())

# Group sales by category
category_sales = df.groupby("Category")["Sales"].sum()

# Print total sales
print(category_sales)

# Create a bar chart
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()
