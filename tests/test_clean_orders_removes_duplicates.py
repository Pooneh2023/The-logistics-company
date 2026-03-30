from src.data.clean_orders import clean_orders
import pandas as pd

def test_clean_orders_removes_duplicates():
    df = pd.DataFrame({
        "Order ID": [1, 1],
        "Value": [10, 10]
    })

    cleaned = clean_orders(df)

    assert len(cleaned) == 1