import re


def is_valid_email(email: str) -> bool:
    """
    Validates if the given email is in the correct format.

    :param email: The email address to validate.
    :return: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))


def is_valid_phone(phone: str) -> bool:
    """
    Validates if the given phone number is in the Brazilian format.

    Acceptable formats:
    - (xx) xxxxx-xxxx
    - (xx) xxxx-xxxx

    :param phone: The phone number to validate.
    :return: True if the phone number is valid, False otherwise.
    """
    phone_regex = r"^\(\d{2}\) (\d{4,5}-\d{4})$"
    return bool(re.match(phone_regex, phone))
