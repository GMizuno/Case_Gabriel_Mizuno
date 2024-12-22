from output.sftp.sftp_connection import SFTPConnection
from output.sftp.error import (
    ConnectionException,
    FileNotFoundError,
)
import re


class SFTPOperations:
    def __init__(self, sftp_connection: SFTPConnection):
        self.sftp_connection = sftp_connection

    def list_files(self, remote_dir: str):
        """Lista os arquivos em um diretório remoto, com tratativa de erros.
        :param remote_dir:
        :return:
        """
        try:
            self.sftp_connection.connect()
            files = self.sftp_connection.connection.listdir(remote_dir)
            print(f"Arquivos em {remote_dir}: {files}")
            return files
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Erro: FileNotFoundError(O diretório remoto '{remote_dir}' não foi encontrado."
            )
        except ConnectionException as e:
            raise ConnectionException(
                f"Erro dConnectionException(e conexão com o SFTP: {e}"
            )
        except Exception as e:
            raise ValueError(f"Erro inesperado ao listar arquivos: {e}")

        finally:
            self.sftp_connection.disconnect()

    def find_files_by_regex(self, remote_dir: str, pattern: str):
        """Procura arquivos em um diretório remoto que correspondam ao regex.
        :param remote_dir:
        :param pattern:
        :return:
        """
        try:
            self.sftp_connection.connect()
            files = self.sftp_connection.connection.listdir(remote_dir)
            matched_files = [file for file in files if re.search(pattern, file)]
            print(f"Arquivos correspondentes ao padrão '{pattern}': {matched_files}")
            return matched_files
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Erro: Diretório remoto '{remote_dir}' não encontrado."
            )
        except re.error as e:
            raise ValueError(f"Erro no padrão regex '{pattern}': {e}")
        except ConnectionException as e:
            raise ConnectionException(f"Erro de conexão com o SFTP: {e}")
        except Exception as e:
            raise Exception(f"Erro inesperado ao buscar arquivos: {e}")

        finally:
            self.sftp_connection.disconnect()

    def upload_file(self, local_path: str, remote_path: str):
        """Realiza upload de arquivo para o servidor SFTP.
        :param local_path:
        :param remote_path:
        """
        try:
            self.sftp_connection.connect()
            self.sftp_connection.connection.put(local_path, remote_path)
            print(f"Arquivo {local_path} carregado para {remote_path}.")
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Erro: Arquivo local '{local_path}' não encontrado."
            )
        except PermissionError:
            raise PermissionError(
                f"Erro: Permissão negada para acessar o caminho '{local_path}'."
            )
        except ConnectionException as e:
            raise ConnectionException(f"Erro de conexão durante o upload: {e}")
        except Exception as e:
            raise ValueError(f"Erro inesperado durante o upload: {e}")
        finally:
            self.sftp_connection.disconnect()

    def download_file(self, remote_path: str, local_path: str):
        """Realiza download de arquivo do servidor SFTP.
        :param remote_path:
        :param local_path:
        """
        try:
            self.sftp_connection.connect()
            self.sftp_connection.connection.get(remote_path, local_path)
            print(f"Arquivo {remote_path} baixado para {local_path}.")
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Erro: Arquivo remoto '{remote_path}' não encontrado."
            )
        except ConnectionException as e:
            raise ConnectionException(f"Erro de conexão durante o download: {e}")
        except PermissionError:
            raise PermissionError(
                f"Erro: Permissão negada para salvar o arquivo em '{local_path}'."
            )
        except Exception as e:
            raise ValueError(f"Erro inesperado durante o download: {e}")
        finally:
            self.sftp_connection.disconnect()
