import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def compute_daily_profit(week, selected_indices_by_day):
    days = []
    profits = []
    counts = []
    
    for day, df_day in week.items():
        df_day = df_day.reset_index(drop=True)
        selected_idx = selected_indices_by_day[day]
        
        # Profit is sum of 'priority' for selected jobs
        day_profit = df_day.loc[selected_idx, "priority"].sum()
        day_count = len(selected_idx)
        
        days.append(day)
        profits.append(day_profit)
        counts.append(day_count)
    
    return days, profits, counts

def plot_profit_and_count(days, profits, counts, title):
    x = np.arange(len(days))
    width = 0.35
    
    fig, ax1 = plt.subplots(figsize=(8, 4))
    
    # Profit bars
    bars1 = ax1.bar(x - width/2, profits, width, label="Total Profit")
    ax1.set_ylabel("Total Profit")
    ax1.set_xticks(x)
    ax1.set_xticklabels(days, rotation=45)
    ax1.set_title(title)
    
    # Jobs count bars (second axis)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(x + width/2, counts, width, label="# Jobs", alpha=0.7)
    ax2.set_ylabel("Number of Jobs")
    
    # Combine legends
    bars = bars1 + bars2
    labels = [b.get_label() for b in bars]
    ax1.legend(bars, labels, loc="upper left")
    
    plt.tight_layout()
    plt.show()