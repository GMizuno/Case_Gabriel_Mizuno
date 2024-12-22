import pandas as pd

from output.api import APIConnection, APIRequests

def send_to_api(endpoint: str, data: pd.DataFrame, api_connection: dict):
    try:
        api_connection = APIConnection(**api_connection)
        api_requests = APIRequests(api_connection)
        data_json  = data.to_json()

        api_requests.post(data_json, endpoint)
    except Exception as e:
        raise ValueError(f"Erro ao enviar dados para API: {e}")
