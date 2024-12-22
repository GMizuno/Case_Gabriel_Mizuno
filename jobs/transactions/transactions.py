from mock import mock_data_transactions
from utils import transform_transaction
from utils.dedup import dedup_transaction
import functions_framework



@functions_framework.cloud_event
def prepare_data():
    transactions = mock_data_transactions()
    transactions = dedup_transaction(transactions)
    transactions = transform_transaction(transactions)

    return transactions
