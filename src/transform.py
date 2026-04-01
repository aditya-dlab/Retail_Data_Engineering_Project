import pandas as pd

def transform_data(data):
    customers = data["customers"]
    orders = data["orders"]
    items = data["order_items"]
    products = data["products"]
    payments = data["payments"]

    # Convert datetime
    orders["order_purchase_timestamp"] = \
        pd.to_datetime(orders["order_purchase_timestamp"])

    # Joins
    df = orders.merge(customers, on="customer_id", how="left")
    df = df.merge(items, on="order_id", how="left")
    df = df.merge(products, on="product_id", how="left")
    df = df.merge(payments, on="order_id", how="left")

    return df