from mock import mock_data_products
import functions_framework

from monitoring.constants import EMAIL_LIST, EMAIL_SENDER
from monitoring.smtp.send_email import send_email
from utils import send_to_api, send_to_sftp


def prepare_data():
    products = mock_data_products()
    return products


@functions_framework.cloud_event
def main():
    try:
        products = prepare_data()
        send_to_api("", products, {})
        send_to_sftp(products, "", {})

    except Exception as e:
        send_email(EMAIL_SENDER, EMAIL_LIST, "Erro no job Clients", str(e), {})
        raise ValueError(f"Erro no job Clients {e}")
    return products
