import pandas as pd
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt

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


#fixing missing values

e_sales_analysis["delivery_days"] = e_sales_analysis["delivery_days"].fillna(0.0)
e_sales_analysis["customer_rating"] = e_sales_analysis["customer_rating"].fillna(0.0)



# print(e_sales_analysis.isna().sum())
# print(e_sales_analysis.dtypes)

# print(e_sales_analysis.isna().sum())   
print("Shape: ", order.shape) 

print("Net_sales Sum: ", order["net_sales"].sum())

print("Profit Sum: ", order["profit"].sum())

print("Order ID: ", order["order_id"].nunique())

print("Customer ID: ", e_sales_analysis["customer_id"].nunique())

print("Net Sales Mean", order["net_sales"].mean())

e_sales_analysis["year"] = e_sales_analysis["order_date"].dt.year
e_sales_analysis["months"] = e_sales_analysis["order_date"].dt.month

yearly_sales = (e_sales_analysis.groupby("year")["net_sales"].sum())
monthly_sales = (e_sales_analysis.groupby("months")["net_sales"].sum())

yearly_profit = (e_sales_analysis.groupby("year")["profit"].sum())

print("Yearly Sales: ")
print(yearly_sales)
print("Yearly Profit: ")
print(yearly_profit)
print("Monthly Sales: ")
print(monthly_sales)

print("Year over Year Growth: ")
print(yearly_sales.pct_change() * 100)

print("Profit Growth: ")
print(yearly_profit.pct_change() * 100)

plt.plot(yearly_sales)
plt.xlabel("yearly_sales")
plt.ylabel("net_sales")
plt.title("Yearly Sales")
plt.show()

plt.plot(monthly_sales)
plt.xlabel("monthly_sales")
plt.ylabel("net_sales")
plt.title("Monthly Sales")
plt.show()

