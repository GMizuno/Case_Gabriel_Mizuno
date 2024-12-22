class APIConnection:
    def __init__(self, base_url: str, client_id: str, client_secret: str):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None

    def authenticate(self):
        """Simula a autenticação e retorna um token estático."""
        try:
            print("Autenticando...")
            self.token = "access_token"
        except Exception as e:
            raise ValueError(f"Erro ao autenticar: {e}")

    def refresh_token(self):
        """Simula a renovação do token."""
        try:
            print("Refresh do token...")
            self.token = "mocked_refreshed_access_token"
        except Exception as e:
            raise ValueError(f"Erro ao refazer o token: {e}")

    def get_headers(self):
        """Retorna cabeçalhos simulados."""
        if not self.token:
            self.authenticate()
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
