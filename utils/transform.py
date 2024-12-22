import pandas as pd
import numpy as np
from utils.validations import (
    is_valid_email,
    is_valid_phone,
)


def replace_missing_email(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace missing email values ("" or None) in the 'email' column with 'Sem Email'.

    :param df: pandas DataFrame
    :return: pandas DataFrame with updated 'email' column
    """
    df["email"] = df["email"].replace(["", None, np.nan], "Sem Email")
    return df


def replace_missing_phone(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace missing email values ("" or None) in the 'email' column with 'Sem Email'.

    :param df: pandas DataFrame
    :return: pandas DataFrame with updated 'email' column
    """
    df["phone"] = df["phone"].replace(["", None, np.nan], "Sem Telefone")
    return df


def filter_missing_or_zero_price(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter rows where the 'price' column is NaN or 0.

    :param df: pandas DataFrame
    :return: pandas DataFrame with rows filtered by 'price' column
    """
    return df[(df["price"].notna()) & (df["price"] != 0)]


def validate_email_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate the 'email' column using the is_valid_email function. Replace invalid values with "Email Invalido".

    :param df: pandas DataFrame
    :param is_valid_email: Function to validate if an email is valid
    :return: pandas DataFrame with invalid emails replaced
    """
    df["email"] = df["email"].apply(
        lambda email: email if is_valid_email(email) else "Email Invalido"
    )
    return df


def validate_phone_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate the 'email' column using the is_valid_email function. Replace invalid values with "Email Invalido".

    :param df: pandas DataFrame
    :param is_valid_email: Function to validate if an email is valid
    :return: pandas DataFrame with invalid emails replaced
    """
    df["phone"] = df["phone"].apply(
        lambda phone: phone if is_valid_phone(phone) else "Email Invalido"
    )
    return df
