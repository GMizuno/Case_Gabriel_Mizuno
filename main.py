from mock import mock_data_clients, mock_data_products, mock_data_transactions
from utils import transform_client, transform_transaction
from utils.dedup import dedup_client, dedup_transaction

def prepare_data():
    products = mock_data_products()
    clients = mock_data_clients()
    transactions = mock_data_transactions()

    transactions = dedup_transaction(transactions)
    clients = dedup_client(clients)

    transactions = transform_transaction(transactions)
    clients = transform_client(clients)
    return clients, products, transactions

def main():
    clients, products, transactions = prepare_data()
    