import backoff

from output.api.error import ClientError, ServerError


def request():
    return {"response": 1, "status": 200}


def raise_for_status(request):
    status_code = request["status"]
    if 400 <= status_code < 500:
        raise ClientError(f"{status_code} Client Error")
    elif 500 <= status_code < 600:
        ServerError(f"{status_code} Server Error")
    else:
        ConnectionError(f"{status_code} Connection Error")


class APIRequests:
    def __init__(self, api_connection):
        self.api_connection = api_connection

    @backoff.on_exception(backoff.expo, Exception, max_tries=10, factor=10)
    def get(self, endpoint: str, params=None):
        """Simula uma requisição GET retornando um dicionário falso."""
        print(f"GET em {endpoint} com parâmetros: {params}")
        response = request()
        raise_for_status(response)
        return {
            "message": "GET request simulada",
            "endpoint": endpoint,
            "params": params,
        }

    @backoff.on_exception(backoff.expo, Exception, max_tries=10, factor=10)
    def post(self, endpoint: str, data):
        """Simula uma requisição POST retornando um dicionário falso."""
        print(f"POST em {endpoint} com dados: {data}")
        response = request()
        raise_for_status(response)
        return {"message": "POST request simulada", "endpoint": endpoint, "data": data}
