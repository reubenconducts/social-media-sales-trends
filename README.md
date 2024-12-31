# social-media-sales-trends
Provides a suite of analytics tools to find correlations between sales trends for a store and trends on social media.

## Requirements

- Python 3.10+
- pip
- pip install -r requirements.txt

## Project Structure  

```
social-media-sales-trends/
│
├── analysis.py               # Main entry point for running the analysis
├── data/
│   ├── youtube_scraper.py    # Code for scraping YouTube data
│   └── tiktok_scraper.py     # Code for scraping TikTok data
│
├── visualizations/
│   ├── plot_time_series.py   # Code for time-series visualization
│   ├── plot_correlation.py   # Code for correlation heatmap
│   └── plot_sales_comparison.py  # Code for comparison of sales by trend type
│
├── preprocessing/
│   ├── clean_inventory.py    # Data cleaning for inventory data
│   ├── clean_sales.py        # Data cleaning for sales data
│   └── process_trends.py     # Processing and matching trend data
│
├── utils/
│   └── helper_functions.py   # Utility functions used across the project
│
└── requirements.txt          # Required Python libraries
```