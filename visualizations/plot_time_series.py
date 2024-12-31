import pandas as pd
import matplotlib.pyplot as plt

def plot_time_series(
    sales_data: pd.DataFrame, 
    youtube_trends: pd.DataFrame, 
    tiktok_trends: pd.DataFrame
) -> None:
    """
    Plot time-series data showing sales and trend events.

    :param sales_data: Cleaned sales data
    :param youtube_trends: Processed YouTube trend data
    :param tiktok_trends: Processed TikTok trend data
    """
    plt.figure(figsize=(10, 6))
    plt.plot(sales_data['Date'], sales_data['Sales'], label="Sales Data")
    plt.scatter(youtube_trends['published_at'], youtube_trends['title'], label="YouTube Trends", color='blue')
    plt.scatter(tiktok_trends['published_at'], tiktok_trends['title'], label="TikTok Trends", color='red')
    plt.legend()
    plt.title("Sales Trends and Trend Events")
    plt.xlabel("Date")
    plt.ylabel("Sales Volume")
    plt.show()
