import pandas as pd

from output.sftp import SFTPOperations, SFTPConnection

def send_to_sftp(data: pd.DataFrame, remota_path: str, sftp_connection: dict):
    try:
        sftp_connection = SFTPConnection(**sftp_connection)
        sftp_operations = SFTPOperations(sftp_connection)
        sftp_operations.upload_file(data, remota_path)
    except Exception as e:
        raise ValueError(f"Erro ao enviar dados para SFTP: {e}")