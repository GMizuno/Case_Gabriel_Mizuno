from monitoring.constants import EMAIL_LIST, EMAIL_SENDER
from mock import mock_data_clients
from monitoring.smtp.send_email import send_email
from utils import transform_client
from utils.dedup import dedup_client
import functions_framework


def prepare_data():
    clients = mock_data_clients()
    clients = dedup_client(clients)
    clients = transform_client(clients)

    return clients

@functions_framework.cloud_event
def main():
    try:
        clients = prepare_data()

        
    except Exception as e:
        send_email(EMAIL_SENDER, EMAIL_LIST, "Erro no job Clients", str(e), {})
        raise ValueError(f"Erro no job Clients {e}")
