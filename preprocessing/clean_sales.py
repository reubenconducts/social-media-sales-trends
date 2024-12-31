import pandas as pd

def clean_sales_data(sales_data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sales data by removing duplicates and handling missing values.

    :param sales_data: Raw sales data as a DataFrame
    :return: Cleaned sales data
    """
    sales_data_clean: pd.DataFrame = sales_data.drop_duplicates(subset=['SKU', 'Date'])
    sales_data_clean = sales_data_clean.fillna(0)  # Replace missing values with 0
    # TODO: Add further cleaning steps
    return sales_data_clean


