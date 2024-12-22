from mock import mock_data_products
import functions_framework


@functions_framework.cloud_event
def prepare_data():
    products = mock_data_products()
    return products
