import pandas as pd


def mock_data_clients() -> pd.DataFrame:
    data = [
        {
            "id": 2,
            "email": "gabrielmizuno@gmail.com",
            "cep": "24346-030",
            "city": "Niteroi",
            "phone": None,
            "date": "2024-12-01",
        },
        {
            "id": 2,
            "email": "gabrielmizuno@outlook.com",
            "cep": "24346030",
            "city": "Rio de Janeiro",
            "phone": None,
            "date": "2024-12-03",
        },
        {
            "id": 1,
            "email": "gabrielperez",
            "cep": None,
            "city": None,
            "phone": None,
            "date": "2024-12-03",
        },
    ]

    return pd.DataFrame(data)
