import pandas as pd


def dedup_transaction(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicates in a Pandas DataFrame based on 'id' and 'product' columns.
    In case of duplicates, the row with the latest 'date' will be kept.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The cleaned DataFrame with duplicates removed.
    """
    return df.sort_values(by="date", ascending=True).drop_duplicates(
        subset=["id", "product"], keep="first"
    )


def dedup_client(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicates in a Pandas DataFrame based on the 'id' column.
    In case of duplicates, the row with the latest 'date' will be kept.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The cleaned DataFrame with duplicates removed.
    """
    return df.sort_values(by="date", ascending=False).drop_duplicates(
        subset=["id"], keep="first"
    )
