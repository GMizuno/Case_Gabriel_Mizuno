import pandas as pd


def mock_data_products() -> pd.DataFrame:
    data = [
        {"id": 1, "name": "Hungry"},
        {"id": 2, "name": "Ouch"},
        {"id": 3, "name": "Hamburge"},
        {"id": 4, "name": "Batata"},
        {"id": 5, "name": "Soda"},
    ]

    return pd.DataFrame(data)
