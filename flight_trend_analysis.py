"""
Extended flight passenger trend analysis (1949–1960).
This script analyzes yearly patterns, monthly seasonality, volatility,
growth behavior, cumulative trends, and outliers — all from the built-in
Seaborn 'flights' dataset. Results include insights and human-readable takeaways.
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = sns.load_dataset("flights")

# Yearly passenger analysis
yearly = df.groupby("year")["passengers"].sum().reset_index()
yearly["growth_pct"] = yearly["passengers"].pct_change() * 100
yearly["moving_avg"] = yearly["passengers"].rolling(window=3).mean()
yearly["volatility"] = yearly["growth_pct"].diff().abs()

# Calculate CAGR
start_val = yearly["passengers"].iloc[0]
end_val = yearly["passengers"].iloc[-1]
years = yearly["year"].iloc[-1] - yearly["year"].iloc[0]
cagr = ((end_val / start_val) ** (1 / years) - 1) * 100

print("\nYEARLY SUMMARY\n")
print(yearly)

print(f"\nCAGR from {yearly['year'].iloc[0]} to {yearly['year'].iloc[-1]}: {cagr:.2f}%\n")

# Monthly pattern analysis
monthly = df.groupby("month")["passengers"].agg(['mean', 'std']).sort_values(by='mean', ascending=False)

print("\nMONTHLY AVERAGES\n")
print(monthly)

# Heatmap data
pivot = df.pivot(index="month", columns="year", values="passengers")

# Z-score based outlier detection
df["z_score"] = df.groupby("month")["passengers"].transform(lambda x: (x - x.mean()) / x.std())
outliers = df[df["z_score"].abs() > 2]

print("\nOUTLIER MONTHS (Z-score > 2):\n")
print(outliers[["year", "month", "passengers", "z_score"]].sort_values(by='z_score', key=abs, ascending=False))

# Year-over-year monthly growth
df_sorted = df.sort_values(by=["month", "year"])
df_sorted["monthly_yoy_growth"] = df_sorted.groupby("month")["passengers"].pct_change() * 100
monthly_growth = df_sorted.groupby("month")["monthly_yoy_growth"].mean().sort_values(ascending=False)

print("\nAVERAGE YoY GROWTH PER MONTH\n")
print(monthly_growth)

# Monthly share of yearly total
monthly_share = df.copy()
yearly_total = df.groupby("year")["passengers"].sum()
monthly_share["year_total"] = monthly_share["year"].map(yearly_total)
monthly_share["monthly_share"] = (monthly_share["passengers"] / monthly_share["year_total"]) * 100

print("\nMONTHLY SHARE OF YEARLY TOTAL (first few rows):\n")
print(monthly_share.head())

# Pivot for stacked bar chart
stacked_data = monthly_share.pivot(index="year", columns="month", values="monthly_share")

# Visualizations

# Yearly trend
plt.figure(figsize=(10, 6))
plt.plot(yearly["year"], yearly["passengers"], marker='o', label="Passengers")
plt.plot(yearly["year"], yearly["moving_avg"], linestyle='--', label="3-Year Moving Avg")
plt.title("Total Passengers per Year (with Moving Average)")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Monthly average and std
monthly["mean"].plot(kind="bar", yerr=monthly["std"], figsize=(12, 6), capsize=4, color="orange")
plt.title("Monthly Avg Passengers with Volatility")
plt.ylabel("Average Passengers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Heatmap
plt.figure(figsize=(14, 7))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Passenger Heatmap: Month vs Year")
plt.tight_layout()
plt.show()

# Outlier scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="year", y="passengers", hue=df["z_score"].abs() > 2, palette={True: "red", False: "gray"})
plt.title("Outlier Months Highlighted")
plt.tight_layout()
plt.show()

# YoY monthly growth
monthly_growth.plot(kind="bar", figsize=(10, 6), color="steelblue")
plt.title("Avg Year-over-Year Monthly Growth")
plt.ylabel("% Growth")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Stacked bar chart for monthly share
stacked_data.plot(kind="bar", stacked=True, figsize=(14, 7), colormap="tab20c")
plt.title("Monthly Share of Total Passengers per Year")
plt.ylabel("Share (%)")
plt.legend(title="Month", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()

# Insights summary
print("\nINSIGHTS SUMMARY:")
print(f"Highest annual passenger count: {yearly['passengers'].max()} in {yearly.loc[yearly['passengers'].idxmax(), 'year']}")
print(f"Month with highest average traffic: {monthly.idxmax()['mean']} ({monthly.max()['mean']:.1f} avg passengers)")
print(f"Highest monthly YoY growth: {monthly_growth.idxmax()} ({monthly_growth.max():.2f}%)")
print(f"Lowest monthly YoY growth: {monthly_growth.idxmin()} ({monthly_growth.min():.2f}%)")
print(f"Total outlier months detected: {len(outliers)}")
print(f"Overall CAGR over 12 years: {cagr:.2f}%")
