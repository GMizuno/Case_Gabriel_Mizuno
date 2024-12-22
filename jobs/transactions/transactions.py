from mock import mock_data_transactions
from monitoring.constants import EMAIL_LIST, EMAIL_SENDER
from monitoring.smtp.send_email import send_email
from utils import send_to_api, send_to_sftp, transform_transaction
from utils.dedup import dedup_transaction
import functions_framework


def prepare_data():
    transactions = mock_data_transactions()
    transactions = dedup_transaction(transactions)
    transactions = transform_transaction(transactions)

    return transactions


@functions_framework.cloud_event
def main():
    try:
        transactions = prepare_data()
        send_to_api("", transactions, {})
        send_to_sftp(transactions, "", {})

    except Exception as e:
        send_email(EMAIL_SENDER, EMAIL_LIST, "Erro no job Transactions", str(e), {})
        raise ValueError(f"Erro no job Transactions {e}")
