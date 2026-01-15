# Customer Transaction Analysis Project
# Author: Shreya Kathiria
# Purpose: Analyse customer transaction data using Python
# Tools: Pandas, NumPy, Matplotlib, Seaborn

# -------------------------------
# Import Required Libraries
# -------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Environment setup successful")

import pandas as pd
import numpy as np

# ------------------------------------
# Step 3: Load + Inspect the Dataset
# ------------------------------------

FILE_NAME = "transactions.csv"

# 1) Load dataset
transactions_data = pd.read_csv(FILE_NAME)

# 2) Standardise column names (CRITICAL FIX)
# Convert to lowercase and replace spaces with underscores
transactions_data.columns = (
    transactions_data.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Now your columns are:
# customer_id, transaction_amount, date, etc.

print("\n--- Standardised Columns ---")
print(list(transactions_data.columns))

# 3) Quick preview
print("\n--- First 5 rows ---")
print(transactions_data.head())

# 4) Dataset info
print("\n--- Info ---")
print(transactions_data.info())

# 5) Missing values
print("\n--- Missing Values ---")
print(transactions_data.isnull().sum())

# ------------------------------------
# Step 3B: Basic Cleaning
# ------------------------------------

# Fill missing gender values
transactions_data["gender"] = transactions_data["gender"].fillna("Unknown")

# Convert date columns to datetime
transactions_data["date"] = pd.to_datetime(
    transactions_data["date"], errors="coerce", dayfirst=True
)

transactions_data["birthdate"] = pd.to_datetime(
    transactions_data["birthdate"], errors="coerce", dayfirst=True
)

# Drop rows with missing critical values
transactions_data = transactions_data.dropna(
    subset=["customer_id", "transaction_amount", "date"]
)

# Remove invalid transaction amounts
transactions_data = transactions_data[
    transactions_data["transaction_amount"] >= 0
]

print("\n--- After Cleaning Shape ---")
print(transactions_data.shape)

print("\n--- After Cleaning Missing Values ---")
print(transactions_data.isnull().sum())

print("\n✅ Step 3 completed successfully")

# Set visual style
sns.set(style="whitegrid")

print("\n--- Transaction Amount Distribution ---")
print(transactions_data["transaction_amount"].describe())

# Histogram of transaction amounts
plt.figure()
sns.histplot(transactions_data["transaction_amount"], bins=40, kde=True)
plt.title("Distribution of Transaction Amounts")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Total spending per category
category_spend = (
    transactions_data
    .groupby("category")["transaction_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Total Spending by Category ---")
print(category_spend)

# Bar chart
plt.figure(figsize=(10, 5))
category_spend.plot(kind="bar")
plt.title("Total Spending by Category")
plt.xlabel("Category")
plt.ylabel("Total Transaction Amount")
plt.tight_layout()
plt.show()


top_merchants = (
    transactions_data
    .groupby("merchant_name")["transaction_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- Top 10 Merchants by Total Spend ---")
print(top_merchants)

plt.figure(figsize=(10, 5))
top_merchants.plot(kind="bar")
plt.title("Top 10 Merchants by Total Transaction Value")
plt.xlabel("Merchant")
plt.ylabel("Total Transaction Amount")
plt.tight_layout()
plt.show()


# Create month column
transactions_data["month"] = transactions_data["date"].dt.to_period("M")

monthly_spend = (
    transactions_data
    .groupby("month")["transaction_amount"]
    .sum()
)

print("\n--- Monthly Spending Trend ---")
print(monthly_spend)

plt.figure(figsize=(10, 5))
monthly_spend.plot()
plt.title("Monthly Transaction Spend Over Time")
plt.xlabel("Month")
plt.ylabel("Total Transaction Amount")
plt.tight_layout()
plt.show()

gender_spend = (
    transactions_data
    .groupby("gender")["transaction_amount"]
    .mean()
)

print("\n--- Average Transaction Amount by Gender ---")
print(gender_spend)

plt.figure()
gender_spend.plot(kind="bar")
plt.title("Average Transaction Amount by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Transaction Amount")
plt.tight_layout()
plt.show()

plt.figure()
sns.boxplot(x=transactions_data["transaction_amount"])
plt.title("Transaction Amount Outliers")
plt.xlabel("Transaction Amount")
plt.tight_layout()
plt.show()

print("\n✅ Step 4 complete: Exploratory Data Analysis finished successfully")
