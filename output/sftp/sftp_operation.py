import pandas as pd

from output.sftp.sftp_connection import SFTPConnection
from output.sftp.error import (
    ConnectionException,
    FileNotFoundError,
)


class SFTPOperations:
    def __init__(self, sftp_connection: SFTPConnection):
        self.sftp_connection = sftp_connection
        
    def upload_file(self, data: pd.DataFrame, remote_path: str):
        """Realiza upload de arquivo para o servidor SFTP.
        :param data:
        :param remote_path:
        """
        try:
            self.sftp_connection.connect()
            print(f"Arquivo {data} carregado para {remote_path}.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Erro: Arquivo local '{data}' não encontrado.")
        except PermissionError:
            raise PermissionError(
                f"Erro: Permissão negada para acessar o caminho '{remote_path}'."
            )
        except ConnectionException as e:
            raise ConnectionException(f"Erro de conexão durante o upload: {e}")
        except Exception as e:
            raise ValueError(f"Erro inesperado durante o upload: {e}")
        finally:
            self.sftp_connection.disconnect()

