import pandas as pd

from utils.transform.transform import (
    replace_missing_email,
    replace_missing_phone,
    validate_email_column,
    validate_phone_column,
)


def transform_client(df: pd.DataFrame) -> pd.DataFrame:
    df_null_remove = replace_missing_email(replace_missing_phone(df))
    df_clean_inconsistencies = validate_phone_column(
        validate_email_column(df_null_remove)
    )

    return df_clean_inconsistencies
