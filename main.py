import subprocess
import pandas as pd
from matplotlib import pyplot as plt

from data_cleaning.data_cleaning import data_cleaning


def show_chart():
    total_tech_count = data_cleaning()
    final_df = (
        pd
        .DataFrame(list(total_tech_count.items()), columns=["Technology", "Count"])
        .sort_values(by="Count", ascending=False)
    )

    final_df = final_df[final_df["Count"] > 1]

    # Explicitly set the backend to "TkAgg" for interactive plotting or "Agg" for PNG rendering
    plt.switch_backend("TkAgg")  # For interactive plots

    # Plot the bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(final_df["Technology"], final_df["Count"], color="skyblue", width=0.9)
    plt.xlabel("Count")
    plt.xticks(rotation=90, fontsize=10)
    plt.ylabel("Technology")
    plt.title("State of market needs in technologies prospective for Python Developer")
    plt.show()


if __name__ == "__main__":
    # Run the spider in a separate process
    spider_process = subprocess.Popen("scrapy crawl vacancies -O jobs.csv", shell=True)

    # Wait for the spider process to finish
    spider_process.wait()

    # Once the spider process finishes, create and display the chart
    show_chart()
