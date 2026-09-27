import pandas as pd
import numpy as np
import matplotlib as mat

# content = None

# with open("customer_master.csv", "r") as f:
#     content = f.read()

data = pd.read_csv("customer_master.csv")

more_data = pd.DataFrame(data)

#finding missing value

# print(data.isna().sum())
# print(data.isna().any())

#finding duplicates

# print(data.duplicated().any(axis=0))

print(more_data.head(5))    

# print(data["customer_id"], data["customer_name"])

#fixing types

print(more_data.columns.values)

print(more_data.dtypes)