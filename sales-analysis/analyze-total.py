import pandas as pd
from helpers import calculate_total, format_currency

df = pd.read_csv("data/sales.csv")

df["totals"] = df["quantity"] * df["price"]
df["formatted total"] = df["totals"].apply(format_currency)

print("Sales data:")
print(df)

grand_total =df["totals"].sum()
print(grand_total)
