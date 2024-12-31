import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional

def plot_sales_comparison(
    sales_data: pd.DataFrame, 
    youtube_trends: pd.DataFrame, 
    tiktok_trends: pd.DataFrame, 
    save_path: Optional[str] = None
) -> None:
    """
    Compare sales before, during, and after trend spikes.

    :param sales_data: Cleaned sales data
    :param youtube_trends: Processed YouTube trend data
    :param tiktok_trends: Processed TikTok trend data
    :param save_path: Optional path to save the plot as an image
    """
    plt.figure(figsize=(10, 6))

    # Example: Summarizing sales and trend data by week
    sales_data['Week'] = pd.to_datetime(sales_data['Date']).dt.to_period('W').astype(str)
    weekly_sales: pd.Series = sales_data.groupby('Week')['Sales'].sum()

    youtube_trends['Week'] = youtube_trends['published_at'].dt.to_period('W').astype(str)
    youtube_trend_counts: pd.Series = youtube_trends.groupby('Week')['title'].count()

    tiktok_trends['Week'] = tiktok_trends['published_at'].dt.to_period('W').astype(str)
    tiktok_trend_counts: pd.Series = tiktok_trends.groupby('Week')['title'].count()

    # Plot sales data
    plt.plot(weekly_sales.index, weekly_sales.values, label="Weekly Sales", marker="o")
    plt.plot(youtube_trend_counts.index, youtube_trend_counts.values, label="YouTube Trends", marker="x")
    plt.plot(tiktok_trend_counts.index, tiktok_trend_counts.values, label="TikTok Trends", marker="s")

    plt.legend()
    plt.title("Weekly Sales vs. Trend Activity")
    plt.xlabel("Week")
    plt.ylabel("Counts")
    if save_path:
        plt.savefig(save_path)
    plt.show()
