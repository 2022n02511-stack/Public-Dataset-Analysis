import pandas as pd
import numpy as np
import matplotlib as mat

# content = None

# with open("customer_master.csv", "r") as f:
#     content = f.read()

customer = pd.read_csv("archive/customer_master.csv")
stats = pd.read_csv("archive/dataset_statistics.csv")
e_sales_analysis = pd.read_csv("archive/ecommerce_sales_customer_analytics_150k.csv")
order = pd.read_csv("archive/order_items.csv")
catalog = pd.read_csv("archive/product_catalog.csv")

data = [customer, stats, e_sales_analysis, order, catalog]

# for item in data:
#     # print("Missing values")
#     # print(item.isna().sum())
#     print("dtypes")
#     print(item.dtypes)
#     print("\n")

#fixing dataypes and cleaning

customer["customer_postal_code"] = customer["customer_postal_code"].astype(str)

# df = stats["Date Range"]

# print(df)

stats[["start_date", "end_date"]] = stats["Date Range"].str.split('to', expand=True)

stats["start_date"] = pd.to_datetime(stats["start_date"])
stats["end_date"] = pd.to_datetime(stats["end_date"])

stats["Total Profit"] = pd.to_numeric(
    stats["Total Profit"].astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False),
    errors='coerce'
)


stats["Total Profit"] = pd.to_numeric(
    stats["Total Profit"].astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False),
    errors='coerce'
)

# print(stats["Average Order Value"])

stats["Average Order Value"] = pd.to_numeric(
    stats["Average Order Value"].astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False),
    errors='coerce'
)

stats["Return Rate"] = stats["Return Rate"].str.replace("%", "", regex=False).astype(float)
stats["Cancellation Rate"] = stats["Cancellation Rate"].str.replace("%", "", regex=False).astype(float)

# print(e_sales_analysis.columns.values)

e_sales_analysis["order_date"] = pd.to_datetime(e_sales_analysis["order_date"])

e_sales_analysis["customer_postal_code"] = e_sales_analysis["customer_postal_code"].astype("str")




print(stats.head())
print(stats.dtypes)

# print(e_sales_analysis.isna().sum())    