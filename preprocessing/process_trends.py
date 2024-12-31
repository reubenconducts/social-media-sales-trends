import pandas as pd
from typing import Tuple

def process_trends_and_match(inventory_data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Process trend data and match it to inventory items.

    :param inventory_data: Cleaned inventory data
    :return: Processed YouTube and TikTok trend data
    """
    # Example placeholder: Replace with scraping and processing logic
    youtube_data = pd.DataFrame({"title": ["Lotus Puzzle"], "published_at": ["2023-12-01"]})
    tiktok_data = pd.DataFrame({"title": ["Christmas Carolers"], "published_at": ["2023-12-02"]})

    youtube_data["relevant_product_match"] = youtube_data["title"].apply(
        lambda title: match_to_inventory(title, inventory_data)
    )
    tiktok_data["relevant_product_match"] = tiktok_data["title"].apply(
        lambda title: match_to_inventory(title, inventory_data)
    )

    return youtube_data, tiktok_data

def match_to_inventory(trend_title: str, inventory_data: pd.DataFrame) -> str:
    """
    Match a trend title to an inventory item.

    :param trend_title: Title of the trend (e.g., video title)
    :param inventory_data: Inventory data
    :return: SKU of the matched product, or 'None' if no match is found
    """
    for _, item in inventory_data.iterrows():
        keywords = f"{item['Description']} {item['Addl Description']}".lower().split()
        if any(keyword in trend_title.lower() for keyword in keywords):
            return item['Item SKU']
    return None
