import pandas as pd


def mock_data_transactions() -> pd.DataFrame:
    data = [
        {
            "id": 1,
            "client_id": 2,
            "product": "Hungry",
            "price": 15,
            "date": "2024-12-01",
        },
        {"id": 1, "client_id": 2, "product": "Ouch", "price": 10, "date": "2024-12-01"},
        {
            "id": 1,
            "client_id": 2,
            "product": "Hungry",
            "price": 15,
            "date": "2024-12-02",
        },
        {
            "id": 2,
            "client_id": 1,
            "product": "Batata",
            "price": 10,
            "date": "2024-12-03",
        },
        {"id": 2, "client_id": 1, "product": "Soda", "price": 5, "date": "2024-12-03"},
    ]

    return pd.DataFrame(data)
