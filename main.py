from monitoring.constants import EMAIL_LIST, EMAIL_SENDER
from mock import mock_data_clients, mock_data_products, mock_data_transactions
from monitoring.smtp.send_email import send_email
from utils import dedup_transaction, transform_client, dedup_client, send_to_api, send_to_sftp, transform_transaction
import os
import json
import sys

TASK_INDEX = os.getenv("CLOUD_RUN_TASK_INDEX", 0)
TASK_ATTEMPT = os.getenv("CLOUD_RUN_TASK_ATTEMPT", 0)
SLEEP_MS = os.getenv("SLEEP_MS", 0)
FAIL_RATE = os.getenv("FAIL_RATE", 0)


def prepare_data_client():
    clients = mock_data_clients()
    clients = dedup_client(clients)
    clients = transform_client(clients)

    return clients

def prepare_data_product():
    products = mock_data_products()
    return products

def prepare_data_transaction():
    transactions = mock_data_transactions()
    transactions = dedup_transaction(transactions)
    transactions = transform_transaction(transactions)

    return transactions


def main():
    
    api_connect_cred = {
        'base_url': 'https://aiquefome/login',
        'client_id': os.environ['API_USER_KEY'],
        'client_secret': os.environ['API_SECERT_KEY'],
    }

    sftp_connect_cred = {
        'host': 'sftp.example.com',
        'key':  os.environ['SFPT_KEY'],
        'port': 22,
    }

    print(os.environ['API_SECERT_KEY'])

    try:
        clients = prepare_data_client()
        send_to_api("", clients, api_connect_cred)
        send_to_sftp(clients, "", sftp_connect_cred)

        products = prepare_data_product()
        send_to_api("", products, api_connect_cred)
        send_to_sftp(products, "", sftp_connect_cred)

        transactions = prepare_data_transaction()
        send_to_api("", transactions, api_connect_cred)
        send_to_sftp(transactions, "", sftp_connect_cred)

        send_email(
            EMAIL_SENDER,
            EMAIL_LIST,
            "Bases de Transação, Produtos e Clientes",
            "Os dados foram enviado para servidor SFTP e API",
            {}
        )

    except Exception as e:
        send_email(EMAIL_SENDER, EMAIL_LIST, "Erro no job Clients", str(e), {})
        raise ValueError(f"Erro no job Clients {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        message = (
                f"Task #{TASK_INDEX}, " + f"Attempt #{TASK_ATTEMPT} failed: {str(err)}"
        )

        print(json.dumps({"message": message, "severity": "ERROR"}))
        sys.exit(1)  # Retry Job Task by exiting the process


