"""
# Hagerty — Acquisition Channel Analysis (starter)

This notebook is just here to get you past setup — it loads the three tables and shows a quick peek so you can start thinking about the problem instead of about file paths. 
**Everything past the peek is yours.** There's no prescribed path, and no need to keep or use these cells as written; rework them however you like.

**Where we're starting:** *which acquisition channels bring in the customers most likely to become paying customers?*

"""

import pandas as pd
import numpy as np

# Three tables, exported from different systems.
customers   = pd.read_csv("customers.csv", parse_dates=["account_created_date"])
transactions = pd.read_csv("transactions.csv", parse_dates=["transaction_date"])
attributes  = pd.read_csv("customer_attributes.csv")


# A quick peek so you know what you're working with.
for name, df in [("customers", customers), ("transactions", transactions), ("attributes", attributes)]:
    print(f"{name}: {df.shape[0]:,} rows x {df.shape[1]} cols")

customers.head()
transactions.head()
attributes.head()