import pandas as pd
import os

RAW_PATH = "data/raw/"

def load_data():
    data = {}

    files = {
        "customers": "olist_customers_dataset.csv",
        "orders": "olist_orders_dataset.csv",
        "order_items": "olist_order_items_dataset.csv",
        "products": "olist_products_dataset.csv",
        "payments": "olist_order_payments_dataset.csv"
    }

    for key, file in files.items():
        path = os.path.join(RAW_PATH, file)
        df = pd.read_csv(path)
        print(f"{file} loaded: {df.shape}")
        data[key] = df

    return data