class SMTPConnection:
    def __init__(self, host: str, port: int, username: str, password: str, use_tls: bool = True):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.use_tls = use_tls
        self.connected = False

    def connect(self):
        """Simula a conexão com o servidor SMTP."""
        try:
            print(f"Simulando conexão com o SMTP em {self.host}:{self.port}...")
            self.connected = True
        except Exception as e:
            raise ValueError(f"Erro ao conectar ao SMTP: {e}")

    def disconnect(self):
        """Simula o encerramento da conexão."""
        if self.connected:
            print("Simulando encerramento da conexão SMTP.")
            self.connected = False
        else:
            print("Nenhuma conexão SMTP ativa para encerrar!")