import pandas as pd

# Load Dataset
df = pd.read_csv("dataset/SampleSuperstore.csv", encoding="latin1")

# First 5 Rows
print("First 5 Rows:")
print(df.head())

# Shape
print("\nDataset Shape:")
print(df.shape)

# Columns
print("\nColumns:")
print(df.columns.tolist())

# Data Types
print("\nData Types:")
print(df.dtypes)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\n-------------------------------")
print("DATA CLEANING")
print("-------------------------------")

# Remove Duplicate Rows
df = df.drop_duplicates()

print("Rows After Removing Duplicates:")
print(df.shape)

# Missing Values After Cleaning
print("\nMissing Values:")
print(df.isnull().sum())

print("\n-------------------------------")
print("SUMMARY STATISTICS")
print("-------------------------------")

print(df.describe())

print("\n-------------------------------")
print("Orders in Each Category")
print("-------------------------------")

print(df["Category"].value_counts())

print("\n-------------------------------")
print("Orders in Each Region")
print("-------------------------------")

print(df["Region"].value_counts())
print("\n-------------------------------")
print("Sales by Category")
print("-------------------------------")

print(df.groupby("Category")["Sales"].sum())

print("\n-------------------------------")
print("Profit by Category")
print("-------------------------------")

print(df.groupby("Category")["Profit"].sum())

import matplotlib.pyplot as plt

# Profit by Category Graph

profit_category = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))

profit_category.plot(
    kind="bar",
    color=["red","green","blue"],
    edgecolor="black"
)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("images/profit_by_category.png", dpi=300)

plt.show()

# -----------------------------
# Sales by Region Graph
# -----------------------------

sales_region = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))

sales_region.plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("images/sales_by_region.png", dpi=300)

plt.show()

# -----------------------------
# Top 10 States by Sales
# -----------------------------

top10_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))

top10_sales.plot(
    kind="bar",
    color="skyblue",
    edgecolor="black"
)

plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("images/top10_states_sales.png", dpi=300)

plt.show()

# -----------------------------
# Top 10 States by Profit
# -----------------------------

top10_profit = df.groupby("State")["Profit"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))

top10_profit.plot(
    kind="bar",
    color="lightgreen",
    edgecolor="black"
)

plt.title("Top 10 States by Profit")
plt.xlabel("State")
plt.ylabel("Profit")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("images/top10_states_profit.png", dpi=300)

plt.show()

# -----------------------------
# Top 10 Sub-Categories by Sales
# -----------------------------

top10_sub_sales = (
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))

top10_sub_sales.plot(
    kind="bar",
    color="cornflowerblue",
    edgecolor="black"
)

plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("images/top10_subcategory_sales.png", dpi=300)

plt.show()

# -----------------------------
# Top 10 Sub-Categories by Profit
# -----------------------------

top10_sub_profit = (
    df.groupby("Sub-Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))

top10_sub_profit.plot(
    kind="bar",
    color="mediumseagreen",
    edgecolor="black"
)

plt.title("Top 10 Sub-Categories by Profit")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("images/top10_subcategory_profit.png", dpi=300)

plt.show()

# -----------------------------
# Discount vs Profit
# -----------------------------

plt.figure(figsize=(8,6))

plt.scatter(
    df["Discount"],
    df["Profit"],
    color="red",
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.grid(True)

plt.tight_layout()

plt.savefig("images/discount_vs_profit.png", dpi=300)

plt.show()

import seaborn as sns

# -----------------------------
# Correlation Heatmap
# -----------------------------

plt.figure(figsize=(8,6))

correlation = df[["Sales", "Quantity", "Discount", "Profit"]].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("images/correlation_heatmap.png", dpi=300)

plt.show()

df.to_csv("dataset/Cleaned_Superstore.csv", index=False)
print("Cleaned Dataset Saved Successfully")

summary = df.describe()

summary.to_csv("dataset/Summary_Report.csv")

print("Summary Report Saved")

category_sales = df.groupby("Category")["Sales"].sum()

category_sales.to_csv("dataset/Category_Sales.csv")

print("Category Sales Saved")

region_sales = df.groupby("Region")["Sales"].sum()

region_sales.to_csv("dataset/Region_Sales.csv")

print("Region Sales Saved")

state_sales = df.groupby("State")["Sales"].sum()

state_sales.to_csv("dataset/State_Sales.csv")

print("State Sales Saved")

sub_sales = df.groupby("Sub-Category")["Sales"].sum()

sub_sales.to_csv("dataset/SubCategory_Sales.csv")

print("Sub Category Sales Saved")

print(df.columns.tolist())

import os

pbix_path = os.path.join(
    os.getcwd(),
    "powerbi",
    "Ecommerce_Sales_Dashboard.pbix"
)

print(pbix_path)   # Path तपासण्यासाठी
print(os.path.exists(pbix_path))  # True किंवा False दाखवेल

os.startfile(pbix_path)

import os

os.startfile("powerbi/Ecommerce_Sales_Dashboard.pbix")