import pandas as pd    
import argparse
from preprocessing.clean_inventory import clean_inventory_data
from preprocessing.clean_sales import clean_sales_data
from preprocessing.process_trends import process_trends_and_match
from visualizations.plot_time_series import plot_sales_trends
from visualizations.plot_correlation import plot_correlation_heatmap
from visualizations.plot_sales_comparison import plot_sales_comparison

def main(inventory_path: str, sales_path: str, save_dir: str) -> None:
    """
    Main entry point for running the analysis.

    :param inventory_path: Path to the inventory data file (CSV)
    :param sales_path: Path to the sales data file (CSV)
    :param save_dir: Directory to save visualizations
    """
    # Load and clean data
    inventory_data = pd.read_csv(inventory_path)
    sales_data = pd.read_csv(sales_path)

    inventory_data = clean_inventory_data(inventory_data)
    sales_data = clean_sales_data(sales_data)

    # Process trends and match to inventory
    youtube_data, tiktok_data = process_trends_and_match(inventory_data)

    # Create visualizations
    plot_sales_trends(sales_data, youtube_data, tiktok_data, save_dir)
    plot_correlation_heatmap(sales_data, youtube_data, tiktok_data, save_dir)
    plot_sales_comparison(sales_data, youtube_data, tiktok_data, save_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run trend and sales analysis.")
    parser.add_argument("--inventory_path", required=True, help="Path to inventory CSV file")
    parser.add_argument("--sales_path", required=True, help="Path to sales CSV file")
    parser.add_argument("--save_dir", required=True, help="Directory to save visualizations")
    args = parser.parse_args()

    main(args.inventory_path, args.sales_path, args.save_dir)
