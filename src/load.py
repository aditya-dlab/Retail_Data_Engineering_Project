from sqlalchemy import create_engine
import os

# Paths
PROCESSED_PATH = "data/processed/"
os.makedirs(PROCESSED_PATH, exist_ok=True)

# DB Connection (update password)
DB_URL = "postgresql://postgres:nahibataunga28@localhost:5432/retail_db"
engine = create_engine(DB_URL)

def save_data(df):
    # ✅ Save CSV (backup/debugging)
    csv_path = os.path.join(PROCESSED_PATH, "master_table.csv")
    df.to_csv(csv_path, index=False)
    print(f"CSV saved at {csv_path}")

    # ✅ Save to PostgreSQL (main storage)
    df.to_sql("master_table", engine, if_exists="replace", index=False)
    print("Data loaded into PostgreSQL")