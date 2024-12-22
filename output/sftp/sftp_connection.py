from output.sftp.error import ConnectionException


def connection(
    host,
    username,
    password,
    port,
): ...

sftp_connect_cred = {
    'host': '111',
    'username': '111',
    'password': '111',
    'port': 111,
}

class SFTPConnection:
    def __init__(self, host: str, username: str, password: str, port: int = 22):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        """Estabelece conexão com o servidor SFTP."""
        try:
            self.connection = connection(
                host=self.host,
                username=self.username,
                password=self.password,
                port=self.port,
            )
            print("Conexão SFTP estabelecida com sucesso!")
        except ConnectionException:
            raise ConnectionException("Erro ao conectar ao SFTP")
        except Exception as e:
            raise ValueError(f"Erro inesperado ao conectar: {e}")

    def disconnect(self):
        """Fecha a conexão com o servidor SFTP."""
        if self.connection:
            self.connection.close()
            print("Conexão SFTP fechada")
        else:
            print("Nenhuma conexão SFTP ativa para fechar!")
