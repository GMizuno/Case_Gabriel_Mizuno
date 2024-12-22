from mock import mock_data_clients
from utils import transform_client
from utils.dedup import dedup_client

def prepare_data():
    clients = mock_data_clients()
    clients = dedup_client(clients)
    clients = transform_client(clients)

    return clients

def main():
    try:
        clients = prepare_data()
    except Exception as e:
        print(f"Erro ao processar dados: {e}")