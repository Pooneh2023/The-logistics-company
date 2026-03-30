from src.data.clean_orders import clean_orders
from src.data.merge_data import merge_data

import pandas as pd

def run_pipeline():
    orders = pd.read_excel("data/raw/Muesli Project raw data.xlsx")

    clean = clean_orders(orders)

    clean.to_excel("data/cleaned/clean_orders.xlsx", index=False)

    final = merge_data()

    final.to_excel("data/final/final_data.xlsx", index=False)

if __name__ == "__main__":
    run_pipeline()