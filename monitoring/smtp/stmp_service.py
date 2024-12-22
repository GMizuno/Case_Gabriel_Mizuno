from monitoring.smtp.smtp_connection import SMTPConnection


class SMTPService:
    def __init__(self, smtp_connection: SMTPConnection):
        self.smtp_connection = smtp_connection

    def send_email(self, sender: str, recipient: str, subject: str, body: str):
        """Simula o envio de um email."""
        self.smtp_connection.connect()
        try:
            print(
                f"Simulando envio de email de {sender} para {recipient}:\n"
                f"Assunto: {subject}\n"
                f"Corpo: {body}"
            )
            self.smtp_connection.disconnect()
        except Exception as e:
            raise ValueError(f"Erro ao enviar email: {e}")

    def send_email_with_attachment(
        self, sender: str, recipient: str, subject: str, body: str, attachment_path: str
    ):
        """Simula o envio de um email com anexo."""
        self.smtp_connection.connect()
        try:
            print(
                f"Simulando envio de email com anexo de {sender} para {recipient}:\n"
                f"Assunto: {subject}\n"
                f"Corpo: {body}\n"
                f"Anexo: {attachment_path} (simulado)"
            )
            self.smtp_connection.disconnect()
        except Exception as e:
            raise ValueError(f"Erro ao enviar email com anexo: {e}")
