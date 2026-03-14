
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("superstore.csv")

print(df.head())

# Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)

plt.figure()
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.show()

# Top Customers
top_customers = df.groupby("Customer_Name")["Sales"].sum().sort_values(ascending=False).head(10)
print(top_customers)
