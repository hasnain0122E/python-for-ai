import pandas as pd
import json
import os

#read csv File
df = pd.read_csv("data/sales.csv")
print("CSV FILES:")
print(df)
print(f"\n shape: {df.shape[0]} rows, {df.shape[1]} columns")

df["total"] = df["quantity"] * df["price"]
print(f"\n With Totals")
print(df)

if not os.path.exists("output"):
    os.makedirs("output")
else:
    print("output folder already exists")

df.to_json("output/sales_data.json", orient="records", indent=2)
df.to_excel("output/sales_data.xlsx", index=False)
df.to_csv("output/sales_data.csv", index=False)