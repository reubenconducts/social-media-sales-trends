import pandas as pd

def clean_inventory_data(inventory_data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean inventory data by removing unnecessary columns and handling missing values.

    :param inventory_data: Raw inventory data as a DataFrame
    :return: Cleaned inventory data
    """
    inventory_data_clean: pd.DataFrame = inventory_data.dropna(subset=['Item SKU', 'Description'])
    # TODO: Add further cleaning steps
    return inventory_data_clean
