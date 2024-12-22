from monitoring import SMTPConnection, SMTPService


def send_email(email_address: list, subject: str, body: str, smtp_connection: dict):
    try:
        smtp_connection = SMTPConnection(**smtp_connection)
        smtp_service = SMTPService(smtp_connection)

        email_address = ','.join(email_address)

        smtp_service.send_email('asdad', email_address, subject, body)
    except Exception as e:
        raise ValueError(f"Erro ao enviar email: {e}")

    
    